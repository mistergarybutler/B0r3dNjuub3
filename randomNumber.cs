//None of the below+1 comments are necessary, and I know there is a better way. I'll figure it out later
//Gary Butler - February 14, 2018
//compile like: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /out:randomNumber.exe .\randomNumber.cs
//run like: .\randomNumber.exe

//using powershell to generate some lines.
//$colors = [System.Enum]::GetNames([System.ConsoleColor])
//$colors | % { Write-Host "`t`t`t`telse if ((fg == $($colors.IndexOf($_))) && (fg != bg))`n`t`t`t`t{`n`t`t`t`t`tConsole.ForegroundColor = ConsoleColor.$_;`n`t`t`t`t}" }
//ctrl+h replace fg with bg
//ctrl+h replace Foreground with Background
//copy-paste
using System;

namespace Top
{
	class Cat
	{
		static void Main(string[] args)
		{
			Random number = new Random();
			while(true)
			{
				int fg = number.Next(0, 15);
				int bg = number.Next(0, 15);

				if ((fg == 0) && (fg != bg))
				{
					Console.ForegroundColor = ConsoleColor.Black;
				}
				
                                else if ((fg == 1) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkBlue;
                                }

                                else if ((fg == 2) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkGreen;
                                }

                                else if ((fg == 3) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkCyan;
                                }

                                else if ((fg == 4) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkRed;
                                }

                                else if ((fg == 5) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkMagenta;
                                }

                                else if ((fg == 6) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                                }

                                else if ((fg == 7) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Gray;
                                }

                                else if ((fg == 8) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.DarkGray;
                                }

                                else if ((fg == 9) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Blue;
                                }

                                else if ((fg == 10) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Green;
                                }

                                else if ((fg == 11) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Cyan;
                                }

                                else if ((fg == 12) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Red;
                                }

                                else if ((fg == 13) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Magenta;
                                }

                                else if ((fg == 14) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.Yellow;
                                }

                                else if ((fg == 15) && (fg != bg))
                                {
                                        Console.ForegroundColor = ConsoleColor.White;
				}



				if ((bg == 0) && (fg != bg))
				{
					Console.BackgroundColor = ConsoleColor.Black;
				}
				
                                else if ((bg == 1) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkBlue;
                                }

                                else if ((bg == 2) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkGreen;
                                }

                                else if ((bg == 3) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkCyan;
                                }

                                else if ((bg == 4) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkRed;
                                }

                                else if ((bg == 5) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkMagenta;
                                }

                                else if ((bg == 6) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkYellow;
                                }

                                else if ((bg == 7) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Gray;
                                }

                                else if ((bg == 8) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.DarkGray;
                                }

                                else if ((bg == 9) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Blue;
                                }

                                else if ((bg == 10) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Green;
                                }

                                else if ((bg == 11) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Cyan;
                                }

                                else if ((bg == 12) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Red;
                                }

                                else if ((bg == 13) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Magenta;
                                }

                                else if ((bg == 14) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.Yellow;
                                }

                                else if ((bg == 15) && (fg != bg))
                                {
                                        Console.BackgroundColor = ConsoleColor.White;
                                }

				Console.Write("{0:X2} ", number.Next() % 256);
			} 
		}
	}
}