using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;

namespace FileRenametoLower
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                foreach (var file in Directory.GetFiles(ConfigurationManager.AppSettings["Path"]))
                {
                    string newname = file.ToLowerInvariant().Replace(" ", "");


                    File.Move(file, newname);
                }

                Console.WriteLine("Completed");
                Console.ReadKey();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

        }
    }
}
