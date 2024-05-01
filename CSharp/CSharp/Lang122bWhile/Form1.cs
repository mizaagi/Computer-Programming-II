namespace Lang122bWhile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("Hours\tPay");
            for (int lcv = 1; lcv < 41; lcv++)
            {
                listBox1.Items.Add(lcv.ToString() + "\t" + (lcv * 4).ToString());
            }
        }
    }
}