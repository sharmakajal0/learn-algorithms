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

        Sequence(const Sequence<T> &to_copy) {
            size = to_copy.size;
            container = new T[size];

            for (int i = 0; i < size; i++)
            {
                container[i] = to_copy.container[i];
            }
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

        Sequence<T> insertion_sort() {
            Sequence<T> sorted_sequence = *this;
            for (int i = 2; i <= sorted_sequence.length(); i++)
            {
                int key = sorted_sequence[i];
                int j = i - 1;

                while (j > 0 && sorted_sequence[j] > key)
                {
                    sorted_sequence[j + 1] = sorted_sequence[j];
                    j = j - 1;
                }
                sorted_sequence[j + 1] = key;
            }

            return sorted_sequence;
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

template <typename T>
Sequence<T> insertion_sort(const Sequence<T> input_sequence){
    Sequence<T> sorted_sequence = input_sequence;
    for (int i = 2; i <= sorted_sequence.length(); i++)
    {
        int key = sorted_sequence[i];
        int j = i - 1;

        while (j > 0 && sorted_sequence[j] > key)
        {
            sorted_sequence[j + 1] = sorted_sequence[j];
            j = j - 1;
        }
        sorted_sequence[j + 1] = key;
    }

    return sorted_sequence;
}
// Template in c++
// Constructors in c++
// Copy Constructors in c++
// `this` pointer in c++
// index operator in c++ - `[]`
int main()
{
    try {

        Sequence<int> A(6);
        
        for (int i = 1; i <= A.length(); i++)
        {
            std::cin >> A[i];
        }

        std::cout << "A: " << A.to_string() << std::endl;
        std::cout <<"Sorted A: " << A.insertion_sort().to_string() << std::endl;
    } catch (const char * e) {
        std::cout << e << std::endl;
    }

    return 0;
}

