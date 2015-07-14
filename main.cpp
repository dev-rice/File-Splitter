#include <iostream>
#include <fstream>
#include <string>

using namespace std;

unsigned long getByteCount(string filename);

int main(int argc, char* argv[]) {
    string filename = "test.file";

    unsigned long byte_count = getByteCount(filename);
    cout << "The file '" << filename << "' is " << byte_count << " bytes\n";

}

unsigned long getByteCount(string filename) {
    ifstream my_file(filename, ios::in|ios::binary|ios::ate);

    if (!my_file) {
        cerr << "Error opening file '" << filename << "'\n";
        return 1;
    }

    unsigned long byte_count = 0;
    my_file.seekg(0, ios::end);
    byte_count = my_file.tellg();

    my_file.close();

    return byte_count;
}
