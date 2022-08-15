from django.db import models

# Create your models here.

class TimeSeriesData(models.Model):
    lon = models.CharField(max_length=140, blank=True, null=False, primary_key=True)
    lat = models.CharField(max_length=140, blank=True, null=False)
    number_20141108 = models.FloatField(db_column='20141108', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20141202 = models.FloatField(db_column='20141202', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20141226 = models.FloatField(db_column='20141226', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150212 = models.FloatField(db_column='20150212', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150308 = models.FloatField(db_column='20150308', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150401 = models.FloatField(db_column='20150401', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150425 = models.FloatField(db_column='20150425', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150519 = models.FloatField(db_column='20150519', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150612 = models.FloatField(db_column='20150612', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150706 = models.FloatField(db_column='20150706', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150730 = models.FloatField(db_column='20150730', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150823 = models.FloatField(db_column='20150823', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20150916 = models.FloatField(db_column='20150916', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20151010 = models.FloatField(db_column='20151010', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20151103 = models.FloatField(db_column='20151103', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20151127 = models.FloatField(db_column='20151127', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20151209 = models.FloatField(db_column='20151209', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20151221 = models.FloatField(db_column='20151221', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160114 = models.FloatField(db_column='20160114', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160126 = models.FloatField(db_column='20160126', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160207 = models.FloatField(db_column='20160207', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160219 = models.FloatField(db_column='20160219', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160302 = models.FloatField(db_column='20160302', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160314 = models.FloatField(db_column='20160314', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160326 = models.FloatField(db_column='20160326', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160407 = models.FloatField(db_column='20160407', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160419 = models.FloatField(db_column='20160419', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160501 = models.FloatField(db_column='20160501', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160513 = models.FloatField(db_column='20160513', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160525 = models.FloatField(db_column='20160525', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160606 = models.FloatField(db_column='20160606', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160630 = models.FloatField(db_column='20160630', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160724 = models.FloatField(db_column='20160724', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160817 = models.FloatField(db_column='20160817', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160910 = models.FloatField(db_column='20160910', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20160922 = models.FloatField(db_column='20160922', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161004 = models.FloatField(db_column='20161004', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161016 = models.FloatField(db_column='20161016', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161028 = models.FloatField(db_column='20161028', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161109 = models.FloatField(db_column='20161109', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161121 = models.FloatField(db_column='20161121', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161203 = models.FloatField(db_column='20161203', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161215 = models.FloatField(db_column='20161215', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20161227 = models.FloatField(db_column='20161227', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170108 = models.FloatField(db_column='20170108', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170114 = models.FloatField(db_column='20170114', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170120 = models.FloatField(db_column='20170120', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170126 = models.FloatField(db_column='20170126', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170201 = models.FloatField(db_column='20170201', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170213 = models.FloatField(db_column='20170213', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170225 = models.FloatField(db_column='20170225', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170309 = models.FloatField(db_column='20170309', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170321 = models.FloatField(db_column='20170321', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170402 = models.FloatField(db_column='20170402', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170414 = models.FloatField(db_column='20170414', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170426 = models.FloatField(db_column='20170426', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170508 = models.FloatField(db_column='20170508', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170520 = models.FloatField(db_column='20170520', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170601 = models.FloatField(db_column='20170601', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170613 = models.FloatField(db_column='20170613', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170625 = models.FloatField(db_column='20170625', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170707 = models.FloatField(db_column='20170707', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170719 = models.FloatField(db_column='20170719', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170731 = models.FloatField(db_column='20170731', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170812 = models.FloatField(db_column='20170812', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170824 = models.FloatField(db_column='20170824', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170905 = models.FloatField(db_column='20170905', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170917 = models.FloatField(db_column='20170917', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20170929 = models.FloatField(db_column='20170929', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171011 = models.FloatField(db_column='20171011', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171023 = models.FloatField(db_column='20171023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171104 = models.FloatField(db_column='20171104', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171116 = models.FloatField(db_column='20171116', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171128 = models.FloatField(db_column='20171128', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171210 = models.FloatField(db_column='20171210', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20171222 = models.FloatField(db_column='20171222', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180103 = models.FloatField(db_column='20180103', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180115 = models.FloatField(db_column='20180115', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180127 = models.FloatField(db_column='20180127', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180208 = models.FloatField(db_column='20180208', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180220 = models.FloatField(db_column='20180220', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180304 = models.FloatField(db_column='20180304', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180316 = models.FloatField(db_column='20180316', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180328 = models.FloatField(db_column='20180328', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180409 = models.FloatField(db_column='20180409', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180421 = models.FloatField(db_column='20180421', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180503 = models.FloatField(db_column='20180503', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180515 = models.FloatField(db_column='20180515', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180527 = models.FloatField(db_column='20180527', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180608 = models.FloatField(db_column='20180608', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180620 = models.FloatField(db_column='20180620', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180702 = models.FloatField(db_column='20180702', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180714 = models.FloatField(db_column='20180714', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180726 = models.FloatField(db_column='20180726', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180807 = models.FloatField(db_column='20180807', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180819 = models.FloatField(db_column='20180819', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180831 = models.FloatField(db_column='20180831', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180912 = models.FloatField(db_column='20180912', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20180924 = models.FloatField(db_column='20180924', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181006 = models.FloatField(db_column='20181006', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181018 = models.FloatField(db_column='20181018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181030 = models.FloatField(db_column='20181030', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181111 = models.FloatField(db_column='20181111', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181117 = models.FloatField(db_column='20181117', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181123 = models.FloatField(db_column='20181123', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181205 = models.FloatField(db_column='20181205', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181217 = models.FloatField(db_column='20181217', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20181229 = models.FloatField(db_column='20181229', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20190110 = models.FloatField(db_column='20190110', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20190122 = models.FloatField(db_column='20190122', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'time_series_data'
        unique_together = [['lon', 'lat']]

class GroundwaterData(models.Model):
    lon = models.CharField(max_length=140, blank=True, null=False, primary_key=True)
    lat = models.CharField(max_length=140, blank=True, null=False)
    number_2016_02_19 = models.FloatField(db_column='2016-02-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_03_02 = models.FloatField(db_column='2016-03-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_03_14 = models.FloatField(db_column='2016-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_03_26 = models.FloatField(db_column='2016-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_04_07 = models.FloatField(db_column='2016-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_04_19 = models.FloatField(db_column='2016-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_05_01 = models.FloatField(db_column='2016-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_05_13 = models.FloatField(db_column='2016-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_05_25 = models.FloatField(db_column='2016-05-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_06_06 = models.FloatField(db_column='2016-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_06_30 = models.FloatField(db_column='2016-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_07_24 = models.FloatField(db_column='2016-07-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_08_17 = models.FloatField(db_column='2016-08-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_09_10 = models.FloatField(db_column='2016-09-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_09_22 = models.FloatField(db_column='2016-09-22', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_10_04 = models.FloatField(db_column='2016-10-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_10_16 = models.FloatField(db_column='2016-10-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_10_28 = models.FloatField(db_column='2016-10-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_11_09 = models.FloatField(db_column='2016-11-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_11_21 = models.FloatField(db_column='2016-11-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_12_03 = models.FloatField(db_column='2016-12-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_12_15 = models.FloatField(db_column='2016-12-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_12_27 = models.FloatField(db_column='2016-12-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_08 = models.FloatField(db_column='2017-01-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_14 = models.FloatField(db_column='2017-01-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_20 = models.FloatField(db_column='2017-01-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_26 = models.FloatField(db_column='2017-01-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_02_01 = models.FloatField(db_column='2017-02-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_02_13 = models.FloatField(db_column='2017-02-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_02_25 = models.FloatField(db_column='2017-02-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_03_09 = models.FloatField(db_column='2017-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_03_21 = models.FloatField(db_column='2017-03-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_04_02 = models.FloatField(db_column='2017-04-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_04_14 = models.FloatField(db_column='2017-04-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_04_26 = models.FloatField(db_column='2017-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_05_08 = models.FloatField(db_column='2017-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_05_20 = models.FloatField(db_column='2017-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_06_01 = models.FloatField(db_column='2017-06-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_06_13 = models.FloatField(db_column='2017-06-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_06_25 = models.FloatField(db_column='2017-06-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_07_07 = models.FloatField(db_column='2017-07-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_07_19 = models.FloatField(db_column='2017-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_07_31 = models.FloatField(db_column='2017-07-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_08_12 = models.FloatField(db_column='2017-08-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_08_24 = models.FloatField(db_column='2017-08-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_09_05 = models.FloatField(db_column='2017-09-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_09_17 = models.FloatField(db_column='2017-09-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_09_29 = models.FloatField(db_column='2017-09-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_10_11 = models.FloatField(db_column='2017-10-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_10_23 = models.FloatField(db_column='2017-10-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_11_04 = models.FloatField(db_column='2017-11-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_11_16 = models.FloatField(db_column='2017-11-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_11_28 = models.FloatField(db_column='2017-11-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_12_10 = models.FloatField(db_column='2017-12-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_12_22 = models.FloatField(db_column='2017-12-22', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_01_03 = models.FloatField(db_column='2018-01-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_01_15 = models.FloatField(db_column='2018-01-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_01_27 = models.FloatField(db_column='2018-01-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_02_08 = models.FloatField(db_column='2018-02-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_02_20 = models.FloatField(db_column='2018-02-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_03_04 = models.FloatField(db_column='2018-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_03_16 = models.FloatField(db_column='2018-03-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_03_28 = models.FloatField(db_column='2018-03-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_09 = models.FloatField(db_column='2018-04-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_21 = models.FloatField(db_column='2018-04-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_03 = models.FloatField(db_column='2018-05-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_15 = models.FloatField(db_column='2018-05-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_27 = models.FloatField(db_column='2018-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_08 = models.FloatField(db_column='2018-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_20 = models.FloatField(db_column='2018-06-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_02 = models.FloatField(db_column='2018-07-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_14 = models.FloatField(db_column='2018-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_26 = models.FloatField(db_column='2018-07-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_08_07 = models.FloatField(db_column='2018-08-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_08_19 = models.FloatField(db_column='2018-08-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_08_31 = models.FloatField(db_column='2018-08-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_09_12 = models.FloatField(db_column='2018-09-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_09_24 = models.FloatField(db_column='2018-09-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_10_06 = models.FloatField(db_column='2018-10-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_10_18 = models.FloatField(db_column='2018-10-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_10_30 = models.FloatField(db_column='2018-10-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_11_11 = models.FloatField(db_column='2018-11-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_11_17 = models.FloatField(db_column='2018-11-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'groundwater_data'
        unique_together = [['lon', 'lat']]

class PrecipitationData(models.Model):
    lon = models.CharField(max_length=140, blank=True, null=False, primary_key=True)
    lat = models.CharField(max_length=140, blank=True, null=False)
    number_2016_01_14 = models.FloatField(db_column='2016-01-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_01_26 = models.FloatField(db_column='2016-01-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_02_07 = models.FloatField(db_column='2016-02-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_02_19 = models.FloatField(db_column='2016-02-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_03_02 = models.FloatField(db_column='2016-03-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_03_14 = models.FloatField(db_column='2016-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_03_26 = models.FloatField(db_column='2016-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_04_07 = models.FloatField(db_column='2016-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_04_19 = models.FloatField(db_column='2016-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_05_01 = models.FloatField(db_column='2016-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_05_13 = models.FloatField(db_column='2016-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_05_25 = models.FloatField(db_column='2016-05-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_06_06 = models.FloatField(db_column='2016-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_06_30 = models.FloatField(db_column='2016-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_07_24 = models.FloatField(db_column='2016-07-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_08_17 = models.FloatField(db_column='2016-08-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_09_10 = models.FloatField(db_column='2016-09-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_09_22 = models.FloatField(db_column='2016-09-22', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_10_04 = models.FloatField(db_column='2016-10-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_10_16 = models.FloatField(db_column='2016-10-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_10_28 = models.FloatField(db_column='2016-10-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_11_09 = models.FloatField(db_column='2016-11-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_11_21 = models.FloatField(db_column='2016-11-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_12_03 = models.FloatField(db_column='2016-12-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_12_15 = models.FloatField(db_column='2016-12-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2016_12_27 = models.FloatField(db_column='2016-12-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_08 = models.FloatField(db_column='2017-01-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_14 = models.FloatField(db_column='2017-01-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_20 = models.FloatField(db_column='2017-01-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_01_26 = models.FloatField(db_column='2017-01-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_02_01 = models.FloatField(db_column='2017-02-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_02_13 = models.FloatField(db_column='2017-02-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_02_25 = models.FloatField(db_column='2017-02-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_03_09 = models.FloatField(db_column='2017-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_03_21 = models.FloatField(db_column='2017-03-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_04_02 = models.FloatField(db_column='2017-04-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_04_14 = models.FloatField(db_column='2017-04-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_04_26 = models.FloatField(db_column='2017-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_05_08 = models.FloatField(db_column='2017-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_05_20 = models.FloatField(db_column='2017-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_06_01 = models.FloatField(db_column='2017-06-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_06_13 = models.FloatField(db_column='2017-06-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_06_25 = models.FloatField(db_column='2017-06-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_07_07 = models.FloatField(db_column='2017-07-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_07_19 = models.FloatField(db_column='2017-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_07_31 = models.FloatField(db_column='2017-07-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_08_12 = models.FloatField(db_column='2017-08-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_08_24 = models.FloatField(db_column='2017-08-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_09_05 = models.FloatField(db_column='2017-09-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_09_17 = models.FloatField(db_column='2017-09-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_09_29 = models.FloatField(db_column='2017-09-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_10_11 = models.FloatField(db_column='2017-10-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_10_23 = models.FloatField(db_column='2017-10-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_11_04 = models.FloatField(db_column='2017-11-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_11_16 = models.FloatField(db_column='2017-11-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_11_28 = models.FloatField(db_column='2017-11-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_12_10 = models.FloatField(db_column='2017-12-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2017_12_22 = models.FloatField(db_column='2017-12-22', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_01_03 = models.FloatField(db_column='2018-01-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_01_15 = models.FloatField(db_column='2018-01-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_01_27 = models.FloatField(db_column='2018-01-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_02_08 = models.FloatField(db_column='2018-02-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_02_20 = models.FloatField(db_column='2018-02-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_03_04 = models.FloatField(db_column='2018-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_03_16 = models.FloatField(db_column='2018-03-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_03_28 = models.FloatField(db_column='2018-03-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_09 = models.FloatField(db_column='2018-04-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_04_21 = models.FloatField(db_column='2018-04-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_03 = models.FloatField(db_column='2018-05-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_15 = models.FloatField(db_column='2018-05-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_05_27 = models.FloatField(db_column='2018-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_08 = models.FloatField(db_column='2018-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_06_20 = models.FloatField(db_column='2018-06-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_02 = models.FloatField(db_column='2018-07-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_14 = models.FloatField(db_column='2018-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_07_26 = models.FloatField(db_column='2018-07-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_08_07 = models.FloatField(db_column='2018-08-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_08_19 = models.FloatField(db_column='2018-08-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_08_31 = models.FloatField(db_column='2018-08-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_09_12 = models.FloatField(db_column='2018-09-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_09_24 = models.FloatField(db_column='2018-09-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_10_06 = models.FloatField(db_column='2018-10-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_10_18 = models.FloatField(db_column='2018-10-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_10_30 = models.FloatField(db_column='2018-10-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_11_11 = models.FloatField(db_column='2018-11-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_11_17 = models.FloatField(db_column='2018-11-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_11_23 = models.FloatField(db_column='2018-11-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_12_05 = models.FloatField(db_column='2018-12-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_12_17 = models.FloatField(db_column='2018-12-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2018_12_29 = models.FloatField(db_column='2018-12-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_01_10 = models.FloatField(db_column='2019-01-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_01_22 = models.FloatField(db_column='2019-01-22', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'precipitation_data'
        unique_together = [['lon', 'lat']]