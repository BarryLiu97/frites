"""Test Auto-Regressive model."""
from frites.simulations import StimSpecAR

AR = ['hga', 'osc_20', 'osc_40', 'osc_40_3', 'ding_2', 'ding_3_indirect',
      'ding_3_direct', 'ding_5']


class TestStimSpecAR(object):
    """docstring for TestStimSpecAR"""

    def test_overall(self):
        kw = dict(n_epochs=5, n_times=100, stim_onset=50)
        model = StimSpecAR()
        for stype in AR:
            # test main definition and plotting
            ar = model.fit(ar_type=stype, **kw)
            model.plot(colorbar=True)
            model.plot(colorbar=False, psd=True)
            # test plotting the model as a network
            model.plot_model()
            # test computing and plotting the covgc / mi
            model.compute_covgc(ar, step=30)
            model.plot_covgc()
            model.plot_covgc(plot_mi=True)
            # test the properties
            model.ar
            model.gc
            model.mi


if __name__ == '__main__':
    TestStimSpecAR().test_overall()
