using System;
using System.Collections.Generic;
using System.Text;

namespace CountingCharacters
{
    class Program
    {
        static void Main(string[] args)
        {
            string exampleString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin." +
                "Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum" +
                "augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus.";

            Dictionary<char, int> dict = new Dictionary<char, int>();

            foreach (char c in exampleString)
            {
                if (!dict.ContainsKey(c))
                    dict[c] = 1;
                else
                    dict[c]++;
            }

            foreach (char c in dict.Keys)
                Console.WriteLine($"{c} : {dict[c]}");

            Console.ReadLine();

        }

    }
}
