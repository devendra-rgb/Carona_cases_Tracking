#include <cstdio>
int main(){
    enum class Race{
        White,Black,Weatish
    };
    Race Value=Race::Weatish;
    switch (Value)
    {
    case (Race::Black):
        printf("you selected Black");
        break;
    case (Race::Weatish):
        printf("You selected Weatish");
        break;
    default:
        break;
    }

}