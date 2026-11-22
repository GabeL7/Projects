// include libraries for file control and other functionality
#include <sys/types.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#define BUF_SIZE 4096
#define OUTPUT_MODE 0700

//main takes input.bmp file and output file
int main(int argc, char* argv[])
{
	int in_fd, out_fd, rd_count, wt_count;
	char buffer[BUF_SIZE];
	// Check if the correct number of arguments is provided
	if (argc != 3) exit(1);

	// Open the input file and create the output file
	in_fd = open(argv[1], O_RDONLY);
	if (in_fd < 0) exit(2);

	out_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, OUTPUT_MODE);
	if (out_fd < 0) exit(3);

	// Skip the first 54 bytes (BMP header) and write to the output file
	if (read(in_fd, buffer, 54) != 54) exit(6);
	if (write(out_fd, buffer, 54) != 54) exit(7);

	// Loop to read the image data, modify it, and write to the output file
	while (1 == 1)
	{
		rd_count = read(in_fd, buffer, BUF_SIZE);

		// Break the loop if no more data is read
		if (rd_count <= 0) break;

		// Modify the green channel (b G r)
		for (size_t i = 0; i < rd_count; i += 3)
			buffer[i + 1] = 0;
		//1 - black, 2 - purple, 3 - darken,

		// Write the modified data to the output file
		wt_count = write(out_fd, buffer, rd_count);

		if (wt_count <= 0) exit(4);
	}
	// Close the input and output files
	close(in_fd); close(out_fd);
	if (rd_count == 0) exit(0); else exit(5);
}

/*
includes for file handling, memory allocation, and other utilities
buf_size -> 4096 bytes to be read/written at once
output_mode -> owner: read, write, and execute permissions (0700), (s,o,g,other)
skips 54-byte BMP header, zeros green values
main takes 2 arguments (i/o)
data storage, read/write, error checking (eof), and i/o
*/
