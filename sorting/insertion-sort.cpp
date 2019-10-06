#include<iostream>
#include<string>
#include<sstream>

template <typename T>
class Sequence {
    private:
        T *container;
        int size;
    public:
        Sequence(int array_size) {
            size = array_size;
            container = new T[size];
        }

        T& operator[] (int index) {
            if (index < 1 || index > size) {
                std::cout << "index: " << index << ", size: " << size << std::endl;
                throw "Out of bounds. Note: index starts at 1 and ends at size";
            }

            return container[index - 1];
        }
        int length() {
            return size;
        }

        std::string to_string() {
            std::stringstream output_stream;

            for(int i = 0; i < size; i++) {
                output_stream << container[i];
                if (i != size -1) {
                    output_stream << " ";
                }
            }

            return output_stream.str();
        }
};

int main()
{
    try {

        Sequence<int> A(6);
        
        for (int i = 1; i <= A.length(); i++)
        {
            std::cin >> A[i];
        }

        std::cout << "Initially: " << A.to_string() << std::endl;

        for (int j = 2; j <= A.length(); j++)
        {
            int key = A[j];
            int i = j - 1;

            while( i > 0 && key < A[i]){
                A[i + 1] = A[i];
                i = i - 1;
            }

            A[i + 1] = key;
            std::cout << "After step: " << j - 1 << ": " << A.to_string() << std::endl;
        }
        std::cout <<"Finally: " << A.to_string() << std::endl;
    } catch (const char * e) {
        std::cout << e << std::endl;
    }

    return 0;
}

