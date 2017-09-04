# include <stdio.h>

int main() {

    int a, ano, k, m, mes, d, dia, n = 0; /*declara variaveis*/
    int i = 1; /*contador*/

    printf ("Digite um numero inteiro: ");
    scanf("%d", &n);

    while (i <= n) {
        printf ("Digite o dia: ");
        scanf("%d", &dia);
        printf ("Digite o mes: ");
        scanf("%d", &mes);
        printf ("Digite o ano: ");
        scanf("%d", &ano);

        a = ano - ((14 - mes) / 12) / 1;
        k = a + ((a / 4) / 1) - ((a / 100) / 1) + ((a / 400) / 1);
        m = mes + 12 * (((14 - mes) / 12) / 1) - 2;
        d = (dia + k + ((31 * m) / 12)/ 1 ) % 7;

        if (d == 0)
            printf("Data %d: %d/%d/%d - domingo\n", i, dia, mes, ano);
        if (d == 1)
            printf("Data %d: %d/%d/%d - segunda-feira\n", i, dia, mes, ano);
        if (d == 2)
            printf("Data %d: %d/%d/%d - terca-feira\n", i, dia, mes, ano);
        if (d == 3)
            printf("Data %d: %d/%d/%d - quarta-feira\n", i, dia, mes, ano);
        if (d == 4)
            printf("Data %d: %d/%d/%d - quinta-feira\n", i, dia, mes, ano);
        if (d == 5)
            printf("Data %d: %d/%d/%d - sexta-feira\n", i, dia, mes, ano);
        if (d == 6)
            printf("Data %d: %d/%d/%d - sabado\n", i, dia, mes, ano);

        i += 1;

    }

    return 0;
}
