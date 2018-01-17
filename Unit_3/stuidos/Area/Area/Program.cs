using System;

namespace Area
{
    class Program
    {
        static void Main(string[] args)
        {
            double r = 0;

            while (true)
            {
                Console.Write("Enter a radius: ");

                string userInput = Console.ReadLine();
                r = double.Parse(userInput);

                if (r > 0)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Radius value can't be 0 or below.");
                    Console.WriteLine("Please retry...");
                    Console.ReadLine();
                }
            }

            double pi = 3.14;
            double area = pi * r * r;

            Console.WriteLine("The area of the circle with radius " + r + " is: " + area);
            Console.ReadLine();
        }
    }
}
