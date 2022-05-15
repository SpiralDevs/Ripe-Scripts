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
    public partial class WinForm_Webhook : Form
    {
        public WinForm_Webhook()
        {
            InitializeComponent();
        }

        private void WinForm_Webhook_Load(object sender, EventArgs e)
        {

        }



        public void SendWebhook()
        {
            string webhook_url = "PUT YOUR WEBHOOK URL FROM DISCORD HERE";
            WebRequest wr = (HttpWebRequest)WebRequest.Create(webhook_url);
            wr.ContentType = "application/json";
            wr.Method = "POST";
            using (var sw = new StreamWriter(wr.GetRequestStream()))
            {
                string json = JsonConvert.SerializeObject(new
                {
                    username = "YOUR WEBHOOK NAME HERE",
                    fields = new[]
                    {
                        new
                        {
                            name = "FIELD NAME",
                            value = "FIELD DESCRIPTION",
                            inline = false, //true or false
                        },
                    },
                    embeds = new[]
                    {
                       new {
                           description = "EMBED DESCRIPTION",
                           title = "EMBED TITLE",
                           url = "https://google.com",//Title URL
                           color = "8464385", //embed color
                           timestamp = DateTime.Now,//current time
                           footer = new {
                               icon_url = "",
                               text = "FOOTER TEXT",
                             },
                         }
                      }
                });
                sw.Write(json);
            }
            var response = (HttpWebResponse)wr.GetResponse();
        }
    }
}