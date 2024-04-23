// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter weight: ");
int weight = int.Parse(Console.ReadLine());
Console.WriteLine("Enter length: ");
int length = int.Parse(Console.ReadLine());
Console.WriteLine("Enter width: ");
int width = int.Parse(Console.ReadLine());
Console.WriteLine("Enter height: ");
int height = int.Parse(Console.ReadLine());

int volume = length * width * height;

if (weight > 27 && volume > 100_000)
    Console.WriteLine("Package is too heavy and too large");
else if (weight > 27)
    Console.WriteLine("Package is too heavy");
else if (volume > 100_000)
    Console.WriteLine("Package is too large");
else
    Console.WriteLine("Package is okay");

Console.ReadLine();
