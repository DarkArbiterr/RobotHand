# RobotHand - Wsteczna Propagacja Błędu

## Opis programu
Program uczy za pomocą wstecznej propagacji błędu model sieci neuronowych MLP w celu przewidywania ruchu ręki robota.
Model uczy się na podstawie zbioru treningowego, który stanowią punkty na ekranie o poniższym kształcie i rozłożeniu:

![Zrzut ekranu 2024-02-01 155629](https://github.com/DarkArbiterr/RobotHand/assets/75552617/7ff7bb02-4570-433e-a1af-8a0388f41914)

Dzięki temu modelowi możemy określać ruch ręki robota dla punktów spoza tego zbioru.

## Model sieci neuronowej MLP i wsteczna propagacja błędu
MLP, czyli Multilayer Perceptron, to model sieci neuronowej która składa się z conajmniej 3 wartw:
* wejściowej
* ukrytej (tych może być więcej niż jedna)
* wyjścowej
W programie użyte są 2 warstwy ukryte, warstwy po kolei mają 2, 10, 6, 2 neurony (w uczeniu na starcie dostajemy współrzędne punktu x i y, na wyjściu chcemy uzyskać rownież 2 wartości - nasz nowy punkt dla ręki robota)
