using System;
using System.Collections.Generic;
using System.Linq;
using Nest;

namespace ElasticSearchWithDotNet
{
    class Program
    {
        //Declaring variables for Node, ConnectionSettings, Client

        public static Uri Node;
        public static ConnectionSettings Settings;
        public static ElasticClient Client;
        static void Main(string[] args)
        {
            try
            {
                // Setting up the node of elastic server
                Node = new Uri("http://localhost:9200/");

                //Passing Node to connection settings ad also setting up the default index
                Settings = new ConnectionSettings(Node).DefaultIndex("my_newblog");

                // Finally setting up the client
                Client = new ElasticClient(Settings);

                // Setting up the number of replicas and shards
                var settings = new IndexSettings { NumberOfReplicas = 1, NumberOfShards = 2 };

                var indexConfig = new IndexState
                {
                    Settings = settings
                };

                // Creating Index if it does not exists
                if (!Client.IndexExists("my_newblog").Exists)
                {
                    Client.CreateIndex("my_newblog", c => c
                    .InitializeUsing(indexConfig)
                    .Mappings(m => m.Map<Post>(mp => mp.AutoMap())));
                }

                // The following lines are methods for various operations using elastic. Comment / Uncomment appropriately

                //InsertData();

                //foreach (var r in PerformTermQuery("blog")) {
                //    Console.WriteLine(r.PostText);
                //}

                //foreach (var r in PerformMatchPhrase("New post from NEST"))
                //{
                //    Console.WriteLine(r.PostText);
                //}


                foreach (var r in PerformTermFilterWithDateGt("blog", DateTime.Now))
                {
                    Console.WriteLine(r.PostText);
                }

                Console.ReadKey();
            }
            catch (Exception ex) {
                Console.Write(ex.Message);
                Console.ReadKey();
            }
        }

        /// <summary>
        /// Method to insert one single post
        /// </summary>
        public static void InsertData()
        {
            var newBlogPost = new Post
            {
                UserId = 1,
                PostDate = DateTime.Now,
                PostText = "New post from NEST"
            };

            Client.IndexDocument(newBlogPost);
        }

        /// <summary>
        /// Method to perform a a term query
        /// </summary>
        /// <param name="searchTerm"></param>
        /// <returns>List of results</returns>
        public static List<Post> PerformTermQuery(string searchTerm) {
            var result = Client.Search<Post>(s => s
            .Query(p => p.Term(q => q.PostText, searchTerm))).Documents.ToList();

            return result;
        }

        /// <summary>
        /// Method to perform a match phrase query
        /// </summary>
        /// <param name="searchText"></param>
        /// <returns>List of results</returns>
        public static List<Post> PerformMatchPhrase(string searchText)
        {
            var result = Client.Search<Post>(s => s
            .Query(p => p.MatchPhrase(q => q.Field("postText").Query(searchText)))).Documents.ToList();

            return result;
        }


        /// <summary>
        /// A complicated term filter which seraches posts greater than a given date.
        /// </summary>
        /// <param name="searchTerm"></param>
        /// <param name="date"></param>
        /// <returns>List of results</returns>
        public static List<Post> PerformTermFilterWithDateGt(string searchTerm, DateTime date)
        {
            var result = Client.Search<Post>(s => s.Query(q => q
           .Bool(bq => bq
           .Filter(
               f => f.Term(q1 => q1.PostText, searchTerm),
               f => f.DateRange(r => r.Name("DateQ").Field(pd =>pd.PostDate).GreaterThan(date))
               )))).Documents.ToList();

            return result;
        }


    }
}

