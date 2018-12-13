using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Configuration;
using System.Threading.Tasks;
using SendGrid;
using SendGrid.Helpers.Mail;

namespace BaahubaliTicketGrabber
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                WebClient client = new WebClient();
                Stream stream = client.OpenRead(ConfigurationManager.AppSettings["TargetSite"]);
                StreamReader reader = new StreamReader(stream);
                String content = reader.ReadToEnd();
                if (content.ToLower().Contains(ConfigurationManager.AppSettings["TargetTheatre"]))
                {
                    SendGrid(ConfigurationManager.AppSettings["EmailtoSend"]).Wait();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        public static async Task SendGrid(string EmailID)
        {
            try
            {
                var client = new SendGridClient(ConfigurationManager.AppSettings["SendGridKey"]);
                var from = new EmailAddress(ConfigurationManager.AppSettings["FromEmailID"], ConfigurationManager.AppSettings["FromEmailDisplayName"]);
                var subject = ConfigurationManager.AppSettings["Subject"];
                var to = new EmailAddress(EmailID, EmailID);
                var plainTextContent = ConfigurationManager.AppSettings["Content"];
                var htmlContent = "<strong>" + ConfigurationManager.AppSettings["Content"] + "</strong>";
                var msg = MailHelper.CreateSingleEmail(from, to, subject, plainTextContent, htmlContent);
                var response = await client.SendEmailAsync(msg);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
