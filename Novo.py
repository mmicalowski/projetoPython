{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mmicalowski/projetoPython/blob/master/Novo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PGYPGCqqymW0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "20ce5664-993b-49f5-ffac-9a3e5cdd409e"
      },
      "source": [
        " \n",
        "nome = input (\"Digite seu nome: \").title()\n",
        "idade = int(input(\"Digite sua idade: \"))\n",
        "print (nome)\n",
        "if idade == 41:\n",
        "  print (\"Que nome lindo\")\n",
        "  print (\"Tem certeza que sua idade é essa?\")\n",
        "  if nome == 'Maicon':\n",
        "    print ('Oi gatão')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome: Maicon Aparecido Micalowski\n",
            "Digite sua idade: 41\n",
            "Maicon Aparecido Micalowski\n",
            "Que nome lindo\n",
            "Tem certeza que sua idade é essa?\n"
          ]
        }
      ]
    }
  ]
}