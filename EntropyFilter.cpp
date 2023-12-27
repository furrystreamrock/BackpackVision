#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
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


double getContrastScore(Mat img, int rows, int cols)
{//calculate how much 'contrast' there are between pixels
	double total_contrast = 0;
	uint8_t *start = img.data;
	int nchannels = 4;
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
						start[(img.step*r) + (nchannels*c) + 4] * start[(img.step*(r+i)) + nchannels*(c+j) + 4] / (255.0*255);
					}
				}
			}
		}
	}
	return total_contrast/(rows-1)/(cols-1);
}


int main()
{
    //std::string image_path = samples::findFile("starry_night.jpg");
    Mat img = imread("./foundim.png", IMREAD_UNCHANGED);
	//std::cout << img.type() <<std::endl;
    imshow("Display window", img);
    //img Mat dimensions are (Row, Col)!!
	//std::cout << img.cols << std::endl << img.rows << std::endl << img.size() << std::endl;
	//std::cout << img.at<int>(1000,2000) <<std::endl; this is correct indexing, row then col
	/* for(int top = 0; top < 4*(img.rows/4); top+= img.rows/4)
		for(int left = 0; left < 4*(img.cols/4); left+= img.cols/4)
			std::cout << top << std::endl; */

	double contrastTest = 0;
	
	contrastTest = getContrastScore(img, img.rows, img.cols);
	std::cout << contrastTest << std::endl;
	int k = waitKey(0); // Wait for a keystroke in the window
    if(k == 's')
    {
        std::cout << " YALLAH";
    }
	return 0;
	
}
