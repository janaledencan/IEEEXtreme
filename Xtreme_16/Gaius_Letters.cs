using System;
using System.Text;
using System.Collections.Generic;
using System.IO;

class Solution {
    
    static void Main(String[] args) {
       
        String sentence;
        StringBuilder result = new StringBuilder();

            sentence = Console.ReadLine();

          for (int i = 0; i < sentence.Length; i++)
            {
                if(sentence[i]>='o' && sentence[i] <= 'z')
                {
                    result.Append(Convert.ToChar(sentence[i] - 12));
                }
                else if (sentence[i] >= 'a' && sentence[i] <= 'l')
                {
                    result.Append(Convert.ToChar(sentence[i] + 14));
                }
                else if (sentence[i] >= 32 && sentence[i] <= 64 || sentence[i] >= 91 && sentence[i] <= 96 || sentence[i] >= 123 && sentence[i] <= 126)
                {
                    result.Append(Convert.ToChar(sentence[i]));
                }
                if (sentence[i] >= 'O' && sentence[i] <= 'Z')
                {
                    result.Append(Convert.ToChar(sentence[i] - 12));
                }
                else if (sentence[i] >= 'A' && sentence[i] <= 'L')
                {
                    result.Append(Convert.ToChar(sentence[i] + 14));
                }
                else if (sentence[i] == 'm')
                {
                    result.Append('a');
                }
                else if (sentence[i] == 'n')
                {
                    result.Append('b');
                }
                else if (sentence[i] == 'M')
                {
                    result.Append('A');
                }
                else if (sentence[i] == 'N')
                {
                    result.Append('B');
                }

            }

            Console.WriteLine(result);
        
        }    
        
}