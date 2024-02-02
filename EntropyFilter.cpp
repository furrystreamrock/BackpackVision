#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

using namespace cv;
//CV READS AS BGR
/* double getPixelDiffSubimg(Mat img, int rows, int cols)
{//finds the 5x5 subimage with highest contrast between pixels
	for(int ch = 0; ch < n
} */
void debug_print_mat(Mat img, int rows, int cols)
{//print image matrix for debugging, absolutely no formatting xD
	std::cout << "step: " << img.step << std::endl;
	uint8_t *start = img.data;
	int nchannels = 4;
	for(int r=0; r<rows; ++r)
	{
		for(int c=0; c<cols; ++c)
		{
			for(int ch=0; ch<nchannels; ++ch)
			{
				uint8_t val = start[(img.step*r) + (nchannels*c) + ch];
				std::cout << int(val) << std::endl;
			}
		}
	}
}


double getContrastScore(Mat img, int rows, int cols, int* has_alpha)
{//calculate how much 'contrast' there are between pixels
	double total_contrast = 0;
	uint8_t *start = img.data;
	int nchannels = 4;
	*has_alpha = 0;
	for(int r=1; r<rows-1; r++)
	{
		for(int c=1; c<cols-1; c++)
		{
			for(int ch=3; ch<nchannels; ch++)
			{
				for(int i = -1; i < 2; i++)
				{
					for(int j = -1; j < 2; j++)
					{
						total_contrast += abs(start[(img.step*r) + (nchannels*c) + ch]- start[(img.step*(r+i)) + nchannels*(c+j) + ch]) * 
						start[(img.step*r) + (nchannels*c) + 3] * start[(img.step*(r+i)) + nchannels*(c+j) + 3] / (255.0*255);
					}
				}
			}
		}
	}
	for(int r=0; r<rows; r++)
	{
		for(int c=0; c<cols; c++)
		{
			//std::cout << int(start[(img.step*r) + (nchannels*c) + 3]) << " ";
			if(start[(img.step*r) + (nchannels*c) + 3] > 5)
				(*has_alpha)++;
		}
	//std::cout << std::endl;
	}
	return total_contrast;
}


int main()
{
	std::string dir_string = "./target_images/FilledTrimmed"; 
	for (const auto& entry : std::filesystem::recursive_directory_iterator(dir_string))
	{
		//std::string file_string = dir_string + std::string(entry); 
		std::string file_name = entry.path().string();
		
	
		Mat img = imread(file_name, IMREAD_UNCHANGED);
		std::cout << file_name.substr(30, file_name.length()) << " " << std::endl;
		Mat copy = img.clone();
		Mat showed;
		resize(copy, showed, Size(copy.cols*4, copy.rows*4), INTER_LINEAR);
		int count = 0;
		int divisions = 6;
		int subSize = 5;
		 
		for(int i = 0; i < divisions; i++)
			for(int j = 0; j < divisions; j++)
			{
				double max_contrast = 0;
				int top = i*img.rows/divisions;
				int left = j*img.cols/divisions;
				int bottom = (i+1)*img.rows/divisions;
				int right =  (j+1)*img.cols/divisions;
				double max_score = -999;
				int loc[2];
				int alpha_num = 0;
				int max_alpha = 0;
				for(int ii = top; ii < bottom - subSize; ii++)
					for(int jj = left;  jj < right - subSize; jj++)
					{
						cv::Range row_subset(ii, ii+subSize);
						cv::Range col_subset(jj, jj+subSize);
						Mat subset = img(row_subset, col_subset);
						double contrastTest = getContrastScore(subset, subset.rows, subset.cols, &alpha_num);
						if(contrastTest > max_score)
						{
							max_alpha = alpha_num;
							max_score = contrastTest;
							loc[0] = ii;
							loc[1] = jj;
						}
					}
									
				Point offset(subSize,subSize);
				Point p1(loc[1], loc[0]);
				Point p2 = p1 + offset*4;			
				Point p3(loc[1]+5, loc[0]+15);
				cv::putText(copy, std::to_string(max_score), p3, cv::FONT_HERSHEY_DUPLEX, .5, CV_RGB(50,100,255), 2);
				cv::rectangle(copy, p1, p2, Scalar(255, 0, 0), 1, 0);
				if(max_alpha > 15)
				{
					std::cout << loc[1] << "," << loc[0] << "   ";
					cv::Range row_subset(loc[0], loc[0]+subSize);
					cv::Range col_subset(loc[1], loc[1]+subSize);
					Mat to_save = img(row_subset, col_subset);
					std::string prefix_folder("./contrastPoints/Raw/");
					std::string png(".png");
					imwrite(prefix_folder + file_name.substr(30, file_name.length()-30-4) + std::to_string(count) + png , to_save);
					count++;
				} 
			}
		std::cout << std::endl; 
// 		imshow("asd", copy);
//		waitKey(5000); 
	}
	return 0; 
    
	
}
