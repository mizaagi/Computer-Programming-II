namespace Pg535CatchMe
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("You got me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
        }

        private string[] strCaption = { "Click here", "Try harder!",
                                        "Try again", "Not even close",
                                        "Where are you?", "I'm over here!",
                                        "Slow, aren't you?"};
        private Random rand = new Random();
    }
}