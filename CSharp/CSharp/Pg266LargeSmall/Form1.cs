namespace Pg266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (int.Parse(textBox1.Text) >= int.Parse(textBox2.Text))
            {
                label4.Text = "Value A is greater than Value B";
            } else
            {
                label4.Text = "Value B is greater than Value A.";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label4.Text = "-";
            textBox1.Text = "";
            textBox2.Text = "";
        }
    }
}