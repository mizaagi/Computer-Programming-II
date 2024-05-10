using Microsoft.VisualBasic;

namespace Pg334LoanCalculator
{
    public partial class Form1 : Form
    {
        const int intMIN_MONTHS = 6;
        const int intMAX_MONTHS = 48;
        const float sngMONTHS_YEAR = 12.0f;

        const double dblNEW_RATE = 0.089;
        const double dblUSED_RATE = 0.095;

        double dblAnnualRate = dblNEW_RATE;

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
            int intCount = 0;
            int intMonths = 0;
            double dblLoan = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dblPrincipal = 0.0;

            intMonths = int.Parse(textBox3.Text);
            dblLoan = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            dblPayment = Financial.Pmt(dblAnnualRate / sngMONTHS_YEAR, intMonths, -dblLoan);
            listBox1.Items.Clear();

            for (intCount = 1; intCount <= intMonths; intCount++)
            {
                string strOut = string.Empty;
                dblInterest = Financial.IPmt(dblAnnualRate / sngMONTHS_YEAR, intCount, intMonths, -dblLoan);
                dblPrincipal = Financial.PPmt(dblAnnualRate / sngMONTHS_YEAR, intCount, intMonths, -dblLoan);

                strOut += "Month: " + intCount;
                strOut += " Payment: " + dblPayment.ToString("$.00");
                strOut += " Interest: " + dblInterest.ToString("$.00");
                strOut += " Principal: " + dblPrincipal.ToString("$.00");
                listBox1.Items.Add(strOut);
            }
        }
    }
}