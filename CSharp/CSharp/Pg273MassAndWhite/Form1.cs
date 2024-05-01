namespace Pg273MassAndWhite
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (int.Parse(textBox1.Text) > 1000) 
            {
                label3.Text = "Too Heavy";
            } else if (int.Parse(textBox1.Text) < 10)
            {
                label3.Text = "Too Light";
            } else
            {
                label3.Text = (int.Parse(textBox1.Text)*9.8).ToString();
            }
        }
    }
}