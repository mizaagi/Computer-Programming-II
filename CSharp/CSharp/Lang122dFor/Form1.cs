namespace Lang122dFor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            for (int lcv = -12; lcv < 17; lcv++)
            {
                listBox1.Items.Add(lcv.ToString() + "\t\t" + Prog122d(lcv).ToString());
            }
        }

        public double Prog122d(double x)
        {
            return Math.Pow(x, 6)
                - (3 * Math.Pow(x, 5))
                - (93 * Math.Pow(x, 4))
                + (87 * Math.Pow(x, 3))
                + (1596 * Math.Pow(x, 2))
                - (1380 * x) - 2800;
        }
    }
}