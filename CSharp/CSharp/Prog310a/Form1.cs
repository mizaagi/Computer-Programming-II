namespace Prog310a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random rand = new Random();

            for (int lcv = 0; lcv < rand.Next(5, 11); lcv++)
            {
                double freq = rand.Next(0, 21) + rand.NextDouble();
                string msg = "";
                int max = (int)Math.Round(freq);
                for (int lcv2 = 0; lcv < max; lcv2++)
                    msg += "*";
                msg += " " + Math.Round(freq, 2);
                listBox1.Items.Add(msg);
            }
        }
    }
}