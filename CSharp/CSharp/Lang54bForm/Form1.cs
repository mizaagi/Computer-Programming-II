namespace Lang54bForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int sum = int.Parse(textBox1.Text) +
                int.Parse(textBox2.Text) +
                int.Parse(textBox3.Text) +
                int.Parse(textBox4.Text);
            double avg = sum / 4.0;
            label6.Text = sum.ToString();
            label8.Text = avg.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label6.Text = "-";
            label8.Text = "-";
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}