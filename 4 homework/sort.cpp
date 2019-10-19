#include <iostream>
using namespace std;
int comb(int *sort, int size)// sort-название массива, size-размер массива,если нужно ввести массив с клавиатуры, то нужно создать динамический массив
{
    int n = 0; // количество перестановок
	int fakt = 1; // фактор уменьшения
	int step = size - 1;

	while (step >= 1)
	{
		for (int i = 0; i + step < size; ++i)
		{
			if (sort[i] > sort[i + step])
			{
				swap(sort[i], sort[i + step]);
				n++;
			}
		}
		step = step - fakt ;
	}
    for (int i  = 0; i < 30; i++)
    {
    return sort[i]; 
    }
}
int main()
{
    int arr[30];
    for (int i  = 0; i < 30; i++)
    {
        arr[i] = rand();
        cout << arr[i] << endl;
    }
    int n = 30;
    comb(arr, n);
    return 0;
}