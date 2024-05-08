namespace Pg435TicketSalesCS
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form frm = new GeneralForm(this);
            frm.Show();
            this.Hide();
        }
    }
}