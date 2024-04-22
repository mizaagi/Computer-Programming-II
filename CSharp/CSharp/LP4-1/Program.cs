// See https://aka.ms/new-console-template for more information
Console.Write("Enter # of copies to be printed: ");
int copies = int.Parse(Console.ReadLine());
double price = 0;
double cost = 0;
// && AND, || OR, ! NOT
if (copies > 0 && copies <= 99) price = 0.30;
else if (copies > 99 && copies <= 499) price = 0.28;
else if (copies > 499 && copies <= 749) price = 0.27;
else if (copies > 749 && copies <= 1000) price = 0.26;
else if (copies > 1000) price = 0.25;
else Console.WriteLine("Invalid number of copies!");

cost = price * copies;
Console.WriteLine("Price per copy is $" + price);
Console.WriteLine("Total cost is $" + Math.Round(cost, 2));
Console.ReadLine();
