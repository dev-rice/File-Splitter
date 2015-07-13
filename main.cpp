#include <iostream>
#include <fstream>
#include <string>

using namespace std;

unsigned long getByteCount(ifstream& file);

int main(int argc, char* argv[]) {
    string filename = "test.file";
    ifstream my_file(filename);

    if (!my_file) {
        cerr << "Error opening file '" << filename << "'\n";
        return 1;
    }

    unsigned long byte_count = getByteCount(my_file);
    cout << "The file '" << filename << "' is " << byte_count << " bytes\n";

    my_file.close();

}

unsigned long getByteCount(ifstream& file) {
    unsigned long byte_count = 0;
    unsigned char current_byte = 0;
    
    while (file >> current_byte) {
        byte_count++;
    }

    return byte_count;
}
