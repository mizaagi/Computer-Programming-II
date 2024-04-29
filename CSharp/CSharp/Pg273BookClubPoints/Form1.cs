namespace Pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (int.Parse(textBox1.Text) == 0)
            {
                label3.Text = "0";
            } else if (int.Parse(textBox1.Text) == 1)
            {
                label3.Text = "5";
            } else if (int.Parse(textBox1.Text) == 2)
            {
                label3.Text = "15";
            } else if (int.Parse(textBox1.Text) == 3)
            {
                label3.Text = "30";
            } else if (int.Parse(textBox1.Text) >= 4)
            {
                label3.Text = "60";
            }
        }
    }
}