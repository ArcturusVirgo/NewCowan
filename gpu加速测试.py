import numpy as np
import cupy as cp


def __complex_cal_gpu(wave: float,
                      new_intensity: np.array,
                      fwhmgauss: float,
                      new_wavelength: np.array,
                      population: np.array,
                      new_J: np.array):
    tt = new_intensity / cp.sqrt(2 * cp.pi) / fwhmgauss * 2.355 * cp.exp(
        -2.355 ** 2 * (new_wavelength - wave) ** 2 / fwhmgauss ** 2 / 2)
    ss = (new_intensity / (2 * new_J + 1)) * 2 * fwhmgauss / (
            2 * cp.pi * ((new_wavelength - wave) ** 2 + cp.power(2 * fwhmgauss, 2) / 4))
    uu = (new_intensity * population / (2 * new_J + 1)) * 2 * fwhmgauss / (
            2 * cp.pi * ((new_wavelength - wave) ** 2 + cp.power(2 * fwhmgauss, 2) / 4))

    return tt.sum(), ss.sum(), uu.sum()


__complex_cal_gpu = cp.cuda.jit()(__complex_cal_gpu)


def complex_cal(wave: float,
                new_intensity: np.array,
                fwhmgauss: float,
                new_wavelength: np.array,
                population: np.array,
                new_J: np.array):
    new_intensity_gpu = cp.asarray(new_intensity)
    new_wavelength_gpu = cp.asarray(new_wavelength)
    population_gpu = cp.asarray(population)
    new_J_gpu = cp.asarray(new_J)

    tt_gpu, ss_gpu, uu_gpu = __complex_cal_gpu(wave, new_intensity_gpu, fwhmgauss, new_wavelength_gpu, population_gpu,
                                               new_J_gpu)

    tt = cp.asnumpy(tt_gpu)
    ss = cp.asnumpy(ss_gpu)
    uu = cp.asnumpy(uu_gpu)

    return tt, ss, uu