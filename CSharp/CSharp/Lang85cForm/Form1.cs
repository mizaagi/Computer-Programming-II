namespace Lang85cForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int birthday = int.Parse(textBox1.Text);
            int number = birthday - 165;
            int finalmonth = number / 100;
            int finalday = number % 100;

            label5.Text = finalmonth.ToString() + "/" + finalday.ToString();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            label5.Text = "-";
            textBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}