# RobotHand - Wsteczna Propagacja Błędu

## Opis programu
Program uczy za pomocą wstecznej propagacji błędu model sieci neuronowych MLP w celu przewidywania ruchu ręki robota.
Model uczy się na podstawie zbioru treningowego, który stanowią punkty na ekranie o poniższym kształcie i rozłożeniu:

![Zrzut ekranu 2024-02-01 155629](https://github.com/DarkArbiterr/RobotHand/assets/75552617/7ff7bb02-4570-433e-a1af-8a0388f41914)

Dzięki temu modelowi możemy określać ruch ręki robota dla punktów spoza tego zbioru.

## Model sieci neuronowej MLP i wsteczna propagacja błędu
### MLP
MLP, czyli Multilayer Perceptron, to model sieci neuronowej która składa się z conajmniej 3 wartw:
> Warstwa wejściowa: każdy neuron reprezentuje jedna wartość cechy (w naszym przypadku wspołrzędne x i y)
> Warstwy ukryte: neurony przetwarzają dane wejściowe, ucząc się reprezentacji cech (może być ich więcej niż jedna)
> Warstwa wyjściowa: generuje wyniki końcowe modelu
W programie użyte są 2 warstwy ukryte. Warstwy po kolei mają 2, 10, 6, 2 neurony (w uczeniu na starcie dostajemy współrzędne punktu x i y, na wyjściu chcemy uzyskać rownież 2 wartości - nasz nowy punkt dla ręki robota)

### Połączenia i funkcja aktywacji
Każde połączenie między neuronami jest opisane wagą, która jest dostosowywana w trakcie treningu sieci. Neurony korzystają
z funkcji aktywacji, która decyduje razem z wagami o wartościach nastepnych warstw. Program wykorzystuje jako funkcję aktywacji sigmoidę:
$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$

### Wsteczna propagacja błędu
Funkcja Forward oblicza kolejno aktywacje i wartości kolejnych warstw aż do wyjściowej. Następnie wykonywana jest wsteczna propagacja błędu - idziemy od końca, od warstwy wyjściowej i wstecz obliczamy błąd. Błąd jest obliczany przez porównanie prognozowanego wyjścia z rzeczywistym. Dla każdego neuronu obliczane są gradienty funkcji błędu względem jego wag.
Wagi są aktualizowane w kierunku przeciwnym do gradientu, co ma na celu zminimalizowanie funkcji błędu. Ten proces uczenia (Forward i Backward), są powtarzane wielokrotnie do uzyskania akcpetowalnego poziomu, lub określoną liczbę iteracji (w programie ustalone jest 1000 iteracji algorytmu).

## Wykres uczenia
Najpierw program wyświetla wykres minimalizacji błędu na przestrzeni iteracji:

![Zrzut ekranu 2024-02-01 155549](https://github.com/DarkArbiterr/RobotHand/assets/75552617/52134a7c-3010-4159-a77f-8de3561bec9d)

## Działanie programu





