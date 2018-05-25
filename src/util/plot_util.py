import os

import matplotlib.pyplot as plt
import numpy as np


def visualize_cost(target_dir):
    stats_path = os.path.join(target_dir, 'stats.tsv')
    data = np.loadtxt(stats_path, delimiter='\t', skiprows=1)
    train_cost = data[:, 1]
    train_ler = data[:, 2]
    val_cost = data[:, 3]
    val_ler = data[:, 4]

    return create_figures(train_cost, train_ler, val_cost, val_ler)


def create_figures(train_cost, train_ler, val_cost, val_ler):
    fig_ctc = plt.figure(figsize=(16, 9))
    ax_ctc = fig_ctc.add_subplot(111)
    ax_ctc.set_title('CTC Loss')
    ax_ctc.set_xlabel('Epoch')
    ax_ctc.set_ylabel('CTC Loss')
    ax_ctc.plot(train_cost)
    ax_ctc.plot(val_cost)

    fig_ler = plt.figure(figsize=(16, 9))
    ax_ler = fig_ler.add_subplot(111)
    ax_ler.set_title('LER Loss')
    ax_ler.set_xlabel('Epochs')
    ax_ler.set_ylabel('LER Loss')
    ax_ler.plot(train_ler)
    ax_ler.plot(val_ler)

    return fig_ctc, fig_ler


def show_plot(target_dir):
    visualize_cost(target_dir)
    plt.show()


if __name__ == '__main__':
    target_dir = r'E:\2018-05-25-08-47-42'
    show_plot(target_dir)