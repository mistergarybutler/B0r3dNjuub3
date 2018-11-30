#include <stdio.h> //standard library
#include <string.h> //string functions
#include <stdlib.h> //for malloc
#include <fcntl.h> //file io
#include <sys/stat.h> //file io
#define MAXBUFF 1000 //a generic maximum size for arrays
#define UCASE_UPPER 90 //in ascii encoding, the last letter of the uppercase alphabet 'Z'
#define LCASE_UPPER 122 //in ascii encoding, the last letter of the lowercase alphabet 'z'
#define ALPHABET_WIDTH 26 //self explanatory

int fd, wl_char=0, i=0, k, arg_ctr=0, ch=0, w=0, hi=0; //integer(4bytes) variables for file descriptor(fd), word list chars(wl_char), cipher text argument array... element iterator (i), rotate iterator for each position in the alphabet (k), an cipher text argument counter (arg_ctr), a temp debug variable for wordlist testing (ch), a var for the number of lines(w)
char *file, word[MAXBUFF], in[MAXBUFF], rotated[MAXBUFF], *p, *wordptr[400000], longword[MAXBUFF]; //char (1byte) for pointer to mem addy of the file name string, array for wordlist words, array for ciphertext arguments, array for rotated plaintext candidates, a pointer for wordlist memory storage locations(*p), a permanent place (array) to hold wordlist words(*wordptr)
unsigned char byte; //a variable (char, 1byte) to hold wordlist characters for testing.

main(int argc, char *argv[]) //main function. 2 function arguments: the argument count and a character array of all the arguments passed on the command line.
{
         if (strcmp(argv[1], "-w") == 0) //if the 1st argument is '-w' perform the statements below.
         { 
             file_array(argv);
             arg_ctr=2; //set the initial argument counter to 2 since not all arguments will be ciphertext.
             
             ct_handler(argc, argv); //run a function which handles the rest of the arguments (ciphertext). Accept 2 function agruments for handling by this and other functions.
         }
         
         else //if the 1st argument is not '-w' just run the ciphertext handler.
         {
             ct_handler(argc, argv); //accepts two arguments as described above.
         }
}

file_array(char *argv[])
{
            int e=0;
            
            file = (char *) malloc(260); //allocate 260 consecutive character sized addresses in memory and return the address of the first one into the pointer 'file'.
            strcpy(file, argv[2]); //copy the 2nd argument to the allocated memory pointed to by 'file'.
            fd = open(file, O_RDONLY); //open the filename string pointed to by the pointer 'file' in read-only mode and return O.S. kernels allocated file handler (integer) for storage in the variable 'fd'.
            printf("File:\t%s\n\n", file); //print the name of the file to stdout for the executer to see.
            
            while(read(fd, &byte, 1) != 0)
            {
                             
                if(byte != '\n')
                {
                     word[e] = byte; //set the word element to the character 'byte'.
                     //printf("%d we:%c b:%c\n", e, word[e], byte); //a test printf
                     e++; //increment to the next element in the array.
                }
                
                else if(byte == '\n')
                {
                    word[e] = '\0'; //put a NULL byte instead of a newline into the array.
                    //printf("%d we:%c b:%c\n", e, word[e], byte); //a test printf
                    p = (char *)malloc(e+1);
                    strcpy(p, word);
                    wordptr[w++] = p;
                    e = 0; //set word element pointer to 0, so we can start a new word.
                }
                
                word[e] = '\0'; //properly terminate the last wordlist word when it is not followed by a newline.
            }            
            close(fd); //close the file descriptor. A.K.A. close the file.
}

ct_handler(int argc, char *argv[]) //funtion ciphertext argument handler.
{
    for (arg_ctr = arg_ctr + 1; arg_ctr <= argc - 1; arg_ctr++) //set the argument counter to arg_ctr (which is either 0 or 2) plus 1. for every test where arg_ctr is less than or equal to the command line argument count - 1, add 1 to arg_ctr and perform the statements below. Quit when arg_ctr > argc - 1.
    {
        strcpy(in, argv[arg_ctr]); //copy the current cipher word into the array 'in'.
        if(strlen(argv[arg_ctr]) > hi);
        {
               hi = strlen(argv[arg_ctr]);
               strcpy(longword, argv[arg_ctr]);
               strcat(longword, "\0");
        }  

        for (k = 1; k < 27; k++) //set the first rotation to 1. for each test where k is less than 27, add one to k.
        {
            rotate(k, argv); //pass k (the current rotation) and the argument vector to the function rotate.
        }
    }
}

rotate(int shift, char *argv[]) //A function to handle individual cipher words and produce their plaintext candidates. The argument shift corresponds to k. The argument *argv[] corresponds to argv (command-line argument vector), which will be used later.
{
	int i; //Don't know why I left this here. This is now a global variable above.
	
	for (i = 0; i <= strlen(in) - 1 && in[i] != EOF && in[i] != '\n'; ++i) //set the cipher word element iterator to 0. While the iterator is less than or equal to the length of the cipherword AND **WTH(the element is not end-of-file or newline)WTH**, increment the iterator by one.
	{    
		if (in[i] > 64 && in[i] < 91) //if argv[i] is between decimal ASCII values for {A...Z}
		{
			if (UCASE_UPPER < in[i] + shift) //if the ASCII value for Z is less than the sum of argv[i] + the rotation(shift)
			{
				rotated[i] = in[i] + shift - ALPHABET_WIDTH; //set rotated[i] to the sum of argv[i] + the rotation(shift) - alphabet size
			}
                        
			else
			{       
				rotated[i] = in[i] + shift; //otherwise set rotated[i] to the sum of argv[i] + the rotation(shift)
			}
		}
 
		else if (in[i] > 96 &&  in[i] < 123) //if argv[i] is between decimal ASCII values for {a...z}
		{
			if (LCASE_UPPER < in[i] + shift) //if the ASCII value for z is less than the sum of argv[i] + the rotation(shift)
			{
				rotated[i] = in[i] + shift - ALPHABET_WIDTH; //set rotated[i] to the sum of argv[i] + the rotation(shift) - alphabet size
			}
 
			else
			{
				rotated[i] = in[i] + shift; //otherwise set rotated[i] to the sum of argv[i] + the rotation(shift)
			}
		}
        
        //else rotated[i] = in[i]; //If not a letter, just output to the rotated array. This is bad for wordlist comparisons.
	}
	rotated[i] = '\0'; //terminate the rotated string with a NULL byte. This is important when we try to read this array. We don't want to read characters from non-clobbered elements of previously longer words.
	//printf("[%d]\t%s\n", shift, rotated);
	
    if(strcmp(argv[1], "-w") == 0) //Since the rotate function is run whether or not we use a wordlist, here we test for '-w' again before we run compare.
    {
       //printf("-w found\n"); //a test printf.
       compare(); //This function accepts no arguments and returns no data to the caller. It simply prints to the screen upon success.
    }             
}

compare(void)
{            
    int i;
             
    for(i = 0; i < w; i++)
    {
        if(strcasecmp(wordptr[i], rotated) == 0) //compare wordlist word with the rotated word.
        {
            printf("[%d] %s\t\t%s\n", k, wordptr[i], rotated); //print the number of the shift, the wordlist word and the rotated word (the plaintext candidate).
        }
    }
}
