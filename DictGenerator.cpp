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



int main()
{
	std::string dir_string = "./target_images/FilledRaw"; 
	for (const auto& entry : std::filesystem::recursive_directory_iterator(dir_string))
	{
		//std::string file_string = dir_string + std::string(entry); 
		std::string file_name = entry.path().string();
		
	
		Mat img = imread(file_name, IMREAD_UNCHANGED);
		uint8_t *start = img.data;
		std::cout << "\"" << file_name.substr(dir_string.length()+1, file_name.length()) << "\": ";
		int count = 0;
		for(int r=0; r<img.rows; ++r)
		{
			for(int c=0; c<img.cols; ++c)
			{
				uint8_t val = start[(img.step*r) + (4*c) + 3];
				if(val > 100)
					count++;		
			}
		}
		std::cout << count  << ",";
		
	}
	return 0; 
    
	
}
