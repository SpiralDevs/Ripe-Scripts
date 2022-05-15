using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
using System.IO;
using System.Net;

namespace Scripts
{
    public partial class WinForm_Notification : Form
    {
        public WinForm_Notification()
        {
            InitializeComponent();
        }

        private void WinForm_Notification_Load(object sender, EventArgs e)
        {

        }

        //Must add a NotifyIcon to the form for notifications
        private void notifyIcon1_BalloonTipClicked(object sender, EventArgs e)
        {
            
        }
        private void Notification()
        {
            notifyIcon1.Visible = true;
            notifyIcon1.ShowBalloonTip(500, "Notification", "This is a notification", ToolTipIcon.Info);
            notifyIcon1.BalloonTipClicked +=   notifyIcon1_BalloonTipClicked;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Notification();
        }
    }
}