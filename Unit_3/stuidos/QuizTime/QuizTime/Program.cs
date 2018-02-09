using System;

namespace QuizTime
{
    class Program
    {
        static void Main(string[] args)
        {
            int choice;
            do
            {
                Console.WriteLine("1. Enter Question\n" +
                                  "2. Take Quiz\n\n");
                Console.Write("Enter Number of Choice: ");
                string input = Console.ReadLine();
                choice = int.Parse(input);

            } while (choice < 1 || choice > 2);

            if (choice == 1)
            {
                // Create new instance passing in value of choice.
                Quiz myQuiz = new Quiz();

                choice = 0;
                do
                {
                    Console.WriteLine("1. Muiltiple Choice\n" +
                                      "2. Checkbox\n" +
                                      "3. True/False\n\n");
                    Console.Write("Enter Number for Type of Question: ");

                } while (choice < 1 || choice > 3);
            }
            

        }

        public class Quiz
        {
            private string question;

            public string question
            {
                get { return question; }
                set { question = value; }
            }

        }

        class MuiltipleChoice : Quiz
        {

        }

        class Checkbox : Quiz
        {

        }

        class TrueFalse : Quiz
        {

        }
    }
}
