#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main() {

    string filename = "elves_inventory.txt";

    int currentElfScore = 0;
    int topElves[3]; //The 3 elves with the most calories
    int sumTopElves; //Variable to store the sum of the top 3 elves

    string line;
    ifstream mFile (filename);

    if(mFile.is_open())
    {
        while(!mFile.eof())
        {
            getline(mFile, line);
            if (line != "") { //If we're not at a blank line, then add the current line to the currentELfTotal

                currentElfScore += stoi(line);

            } else { //If we're at a blank line, we know that we have finished adding up an Elf's inventory

                //Iterate over the topElves list and check if the currentElfScore is greater than any of the top 3 elves
                //If it is, set that position to the currentElfScore and break from the loop
                for (int i = 0; i < 3; i++) {
                    if (currentElfScore > topElves[i]) {
                        topElves[i] = currentElfScore;
                        break;
                    }
                }
                currentElfScore = 0;
            }
        }
        mFile.close();
    }
    else
        cout << "Couldn't open the file" << endl;

    sumTopElves = topElves[0] + topElves[1] + topElves[2];
    cout << "The elf with the most calories has: " << topElves[0] << endl;
    cout << "The sum of the top 3 elves' inventories is: " << sumTopElves << endl;
}