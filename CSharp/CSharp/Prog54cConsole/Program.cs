using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prog54cConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter radius: ");
            double rad = double.Parse(Console.ReadLine());
            double circum = 2 * 3.14 * rad;
            double area = (rad * rad) * 3.14;
            Console.WriteLine("Circumference: " + circum);
            Console.WriteLine("Area: " + area);
            Console.ReadKey();
        }
    }
}
