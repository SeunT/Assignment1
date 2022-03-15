# This is a item Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import numpy as np


if __name__ == '__main__':

    a_whole = {}
    a_morning = {}
    a_night = {}
    m_whole = {}
    m_morning = {}
    m_night = {}
    auto_day_p = {
        '_180': [],
        '_250': [],
        '_70_180': [],
        '_70_150': [],
        '_70': [],
        '_54': []
    }
    a_morning_p = {
        '_180': [],
        '_250': [],
        '_70_180': [],
        '_70_150': [],
        '_70': [],
        '_54': []
    }
    a_night_p = {
        '_180': [],
        '_250': [],
        '_70_180': [],
        '_70_150': [],
        '_70': [],
        '_54': []
    }
    manual_day_p = {
        '_180': [],
        '_250': [],
        '_70_180': [],
        '_70_150': [],
        '_70': [],
        '_54': []
    }
    m_morning_p = {
        '_180': [],
        '_250': [],
        '_70_180': [],
        '_70_150': [],
        '_70': [],
        '_54': []
    }
    m_night_p = {
        '_180': [],
        '_250': [],
        '_70_180': [],
        '_70_150': [],
        '_70': [],
        '_54': []
    }
    indicator = -1

    CGM = pd.read_csv(os.path.join(os.getcwd(), "CGMData.csv"))
    Insulin = pd.read_csv(os.path.join(os.getcwd(), "InsulinData.csv"))

    for i, row in Insulin.iterrows():
        if row['Alarm'] == "AUTO MODE ACTIVE PLGM OFF":
            indicator = row['Date']
            break


    current_day = []
    morning = []
    night = []
    for i, row in CGM.iterrows():
        if row['Date'] == CGM.iloc[i - 1]['Date'] or i == 0:
            current_day.append(i)

            day = row['Date']
            time = row['Time']
            midnight = datetime.strptime(day, "%m/%d/%Y") + relativedelta(days=+1)
            begin = datetime.strptime(f"{day} 6:00:00", "%m/%d/%Y %H:%M:%S")
            new_time = datetime.strptime(f"{day} {time}", "%m/%d/%Y %H:%M:%S")
            if begin < new_time < midnight:
                morning.append(i)
            elif new_time < begin:
                night.append(i)
        else:

            if 277 < len(current_day) < 289:
                if CGM.iloc[i - 1]['Date'] != indicator:

                    if datetime.strptime(row['Date'], "%m/%d/%Y") > datetime.strptime(indicator, "%m/%d/%Y"):
                        a_whole[f"{CGM.iloc[i - 1]['Date']}"] = current_day
                        a_morning[f"{CGM.iloc[i - 1]['Date']}"] = morning
                        a_night[f"{CGM.iloc[i - 1]['Date']}"] = night
                    else:
                        m_whole[f"{CGM.iloc[i - 1]['Date']}"] = current_day
                        m_morning[f"{CGM.iloc[i - 1]['Date']}"] = morning
                        m_night[f"{CGM.iloc[i - 1]['Date']}"] = night

            current_day = [i]
            morning = []
            night = []

            day = row['Date']
            time = row['Time']
            midnight = datetime.strptime(day, "%m/%d/%Y") + relativedelta(days=+1)
            begin = datetime.strptime(f"{day} 6:00:00", "%m/%d/%Y %H:%M:%S")
            new_time = datetime.strptime(f"{day} {time}", "%m/%d/%Y %H:%M:%S")
            if begin < new_time < midnight:
                morning.append(i)
            elif new_time < begin:
                night.append(i)

    for day, value in a_whole.items():
        g_180 = []
        g_250 = []
        i_70_180 = []
        i_70_150 = []
        l_70 = []
        l_54 = []

        for v in value:
            level = CGM.iloc[v]['Sensor Glucose (mg/dL)']
            if level > 180:
                g_180.append(v)
            if level > 250:
                g_250.append(v)
            if 70 <= level <= 180:
                i_70_180.append(v)
            if 70 <= level <= 150:
                i_70_150.append(v)
            if level < 70:
                l_70.append(v)
            if level < 54:
                l_54.append(v)

        _180 = len(g_180) * 100 / 288
        _250 = len(g_250) * 100 / 288
        _70_180 = len(i_70_180) * 100 / 288
        _70_150 = len(i_70_150) * 100 / 288
        _70 = len(l_70) * 100 / 288
        _54 = len(l_54) * 100 / 288
        auto_day_p['_180'].append(_180)
        auto_day_p['_250'].append(_250)
        auto_day_p['_70_180'].append(_70_180)
        auto_day_p['_70_150'].append(_70_150)
        auto_day_p['_70'].append(_70)
        auto_day_p['_54'].append(_54)

    for day, value in a_morning.items():
        g_180 = []
        g_250 = []
        i_70_180 = []
        i_70_150 = []
        l_70 = []
        l_54 = []

        for v in value:
            level = CGM.iloc[v]['Sensor Glucose (mg/dL)']
            if level > 180:
                g_180.append(v)
            if level > 250:
                g_250.append(v)
            if 70 <= level <= 180:
                i_70_180.append(v)
            if 70 <= level <= 150:
                i_70_150.append(v)
            if level < 70:
                l_70.append(v)
            if level < 54:
                l_54.append(v)

        _180 = len(g_180) * 100 / 288
        _250 = len(g_250) * 100 / 288
        _70_180 = len(i_70_180) * 100 / 288
        _70_150 = len(i_70_150) * 100 / 288
        _70 = len(l_70) * 100 / 288
        _54 = len(l_54) * 100 / 288
        a_morning_p['_180'].append(_180)
        a_morning_p['_250'].append(_250)
        a_morning_p['_70_180'].append(_70_180)
        a_morning_p['_70_150'].append(_70_150)
        a_morning_p['_70'].append(_70)
        a_morning_p['_54'].append(_54)

    for day, value in a_night.items():
        g_180 = []
        g_250 = []
        i_70_180 = []
        i_70_150 = []
        l_70 = []
        l_54 = []

        for v in value:
            level = CGM.iloc[v]['Sensor Glucose (mg/dL)']
            if level > 180:
                g_180.append(v)
            if level > 250:
                g_250.append(v)
            if 70 <= level <= 180:
                i_70_180.append(v)
            if 70 <= level <= 150:
                i_70_150.append(v)
            if level < 70:
                l_70.append(v)
            if level < 54:
                l_54.append(v)

        _180 = len(g_180) * 100 / 288
        _250 = len(g_250) * 100 / 288
        _70_180 = len(i_70_180) * 100 / 288
        _70_150 = len(i_70_150) * 100 / 288
        _70 = len(l_70) * 100 / 288
        _54 = len(l_54) * 100 / 288
        a_night_p['_180'].append(_180)
        a_night_p['_250'].append(_250)
        a_night_p['_70_180'].append(_70_180)
        a_night_p['_70_150'].append(_70_150)
        a_night_p['_70'].append(_70)
        a_night_p['_54'].append(_54)

    for day, value in m_whole.items():
        g_180 = []
        g_250 = []
        i_70_180 = []
        i_70_150 = []
        l_70 = []
        l_54 = []

        for v in value:
            level = CGM.iloc[v]['Sensor Glucose (mg/dL)']
            if level > 180:
                g_180.append(v)
            if level > 250:
                g_250.append(v)
            if 70 <= level <= 180:
                i_70_180.append(v)
            if 70 <= level <= 150:
                i_70_150.append(v)
            if level < 70:
                l_70.append(v)
            if level < 54:
                l_54.append(v)

        _180 = len(g_180) * 100 / 288
        _250 = len(g_250) * 100 / 288
        _70_180 = len(i_70_180) * 100 / 288
        _70_150 = len(i_70_150) * 100 / 288
        _70 = len(l_70) * 100 / 288
        _54 = len(l_54) * 100 / 288
        manual_day_p['_180'].append(_180)
        manual_day_p['_250'].append(_250)
        manual_day_p['_70_180'].append(_70_180)
        manual_day_p['_70_150'].append(_70_150)
        manual_day_p['_70'].append(_70)
        manual_day_p['_54'].append(_54)

    for day, value in m_morning.items():
        g_180 = []
        g_250 = []
        i_70_180 = []
        i_70_150 = []
        l_70 = []
        l_54 = []

        for v in value:
            level = CGM.iloc[v]['Sensor Glucose (mg/dL)']
            if level > 180:
                g_180.append(v)
            if level > 250:
                g_250.append(v)
            if 70 <= level <= 180:
                i_70_180.append(v)
            if 70 <= level <= 150:
                i_70_150.append(v)
            if level < 70:
                l_70.append(v)
            if level < 54:
                l_54.append(v)

        _180 = len(g_180) * 100 / 288
        _250 = len(g_250) * 100 / 288
        _70_180 = len(i_70_180) * 100 / 288
        _70_150 = len(i_70_150) * 100 / 288
        _70 = len(l_70) * 100 / 288
        _54 = len(l_54) * 100 / 288
        m_morning_p['_180'].append(_180)
        m_morning_p['_250'].append(_250)
        m_morning_p['_70_180'].append(_70_180)
        m_morning_p['_70_150'].append(_70_150)
        m_morning_p['_70'].append(_70)
        m_morning_p['_54'].append(_54)

    for day, value in m_night.items():
        g_180 = []
        g_250 = []
        i_70_180 = []
        i_70_150 = []
        l_70 = []
        l_54 = []

        for v in value:
            level = CGM.iloc[v]['Sensor Glucose (mg/dL)']
            if level > 180:
                g_180.append(v)
            if level > 250:
                g_250.append(v)
            if 70 <= level <= 180:
                i_70_180.append(v)
            if 70 <= level <= 150:
                i_70_150.append(v)
            if level < 70:
                l_70.append(v)
            if level < 54:
                l_54.append(v)

        _180 = len(g_180) * 100 / 288
        _250 = len(g_250) * 100 / 288
        _70_180 = len(i_70_180) * 100 / 288
        _70_150 = len(i_70_150) * 100 / 288
        _70 = len(l_70) * 100 / 288
        _54 = len(l_54) * 100 / 288

        m_night_p['_180'].append(_180)
        m_night_p['_250'].append(_250)
        m_night_p['_70_180'].append(_70_180)
        m_night_p['_70_150'].append(_70_150)
        m_night_p['_70'].append(_70)
        m_night_p['_54'].append(_54)

    results = {
        '[Night](CGM > 180 mg/dL)': [],
        '[Night](CGM > 250 mg/dL)': [],
        '[Night](CGM >= 70 mg/dL and CGM <= 180 mg/dL)': [],
        '[Night](CGM >= 70 mg/dL and CGM <= 150 mg/dL)': [],
        '[Night](CGM < 70 mg/dL)': [],
        '[Night](CGM < 54 mg/dL)': [],

        '[Morning](CGM > 180 mg/dL)': [],
        '[Morning](CGM > 250 mg/dL)': [],
        '[Morning](CGM >= 70 mg/dL and CGM <= 180 mg/dL)': [],
        '[Morning](CGM >= 70 mg/dL and CGM <= 150 mg/dL)': [],
        '[Morning](CGM < 70 mg/dL)': [],
        '[Morning](CGM < 54 mg/dL)': [],

        '[Full Day](CGM > 180 mg/dL)': [],
        '[Full Day](CGM > 250 mg/dL)': [],
        '[Full Day](CGM >= 70 mg/dL and CGM <= 180 mg/dL)': [],
        '[Full Day](CGM >= 70 mg/dL and CGM <= 150 mg/dL)': [],
        '[Full Day](CGM < 70 mg/dL)': [],
        '[Full Day](CGM < 54 mg/dL)': [],
        'end': [],
    }

    for val, lst in manual_day_p.items():
        sum = 0
        for item in lst:
            sum += item
        avg = sum / len(lst)

        if val == '_180':
            results['[Full Day](CGM > 180 mg/dL)'].append(avg)
        elif val == '_250':
            results['[Full Day](CGM > 250 mg/dL)'].append(
                avg)
        elif val == '_70_180':
            results['[Full Day](CGM >= 70 mg/dL and CGM <= 180 mg/dL)'].append(
                avg)
        elif val == '_70_150':
            results['[Full Day](CGM >= 70 mg/dL and CGM <= 150 mg/dL)'].append(
                avg)
        elif val == '_70':
            results['[Full Day](CGM < 70 mg/dL)'].append(avg)
        elif val == '_54':
            results['[Full Day](CGM < 54 mg/dL)'].append(avg)

    for val, lst in m_morning_p.items():
        sum = 0
        for item in lst:
            sum += item
        avg = sum / len(lst)

        if val == '_180':
            results['[Morning](CGM > 180 mg/dL)'].append(avg)
        elif val == '_250':
            results['[Morning](CGM > 250 mg/dL)'].append(
                avg)
        elif val == '_70_180':
            results['[Morning](CGM >= 70 mg/dL and CGM <= 180 mg/dL)'].append(
                avg)
        elif val == '_70_150':
            results['[Morning](CGM >= 70 mg/dL and CGM <= 150 mg/dL)'].append(
                avg)
        elif val == '_70':
            results['[Morning](CGM < 70 mg/dL)'].append(avg)
        elif val == '_54':
            results['[Morning](CGM < 54 mg/dL)'].append(avg)

    for val, lst in m_night_p.items():
        sum = 0
        for item in lst:
            sum += item
        avg = sum / len(lst)

        if val == '_180':
            results['[Night](CGM > 180 mg/dL)'].append(avg)
        elif val == '_250':
            results['[Night](CGM > 250 mg/dL)'].append(avg)
        elif val == '_70_180':
            results['[Night](CGM >= 70 mg/dL and CGM <= 180 mg/dL)'].append(
                avg)
        elif val == '_70_150':
            results['[Night](CGM >= 70 mg/dL and CGM <= 150 mg/dL)'].append(
                avg)
        elif val == '_70':
            results['[Night](CGM < 70 mg/dL)'].append(avg)
        elif val == '_54':
            results['[Night](CGM < 54 mg/dL)'].append(avg)

    for val, lst in auto_day_p.items():
        sum = 0
        for item in lst:
            sum += item
        avg = sum / len(lst)

        if val == '_180':
            results['[Full Day](CGM > 180 mg/dL)'].append(avg)
        elif val == '_250':
            results['[Full Day](CGM > 250 mg/dL)'].append(
                avg)
        elif val == '_70_180':
            results['[Full Day](CGM >= 70 mg/dL and CGM <= 180 mg/dL)'].append(
                avg)
        elif val == '_70_150':
            results['[Full Day](CGM >= 70 mg/dL and CGM <= 150 mg/dL)'].append(
                avg)
        elif val == '_70':
            results['[Full Day](CGM < 70 mg/dL)'].append(avg)
        elif val == '_54':
            results['[Full Day](CGM < 54 mg/dL)'].append(avg)

    for val, lst in a_morning_p.items():
        sum = 0
        for item in lst:
            sum += item
        avg = sum / len(lst)

        if val == '_180':
            results['[Morning](CGM > 180 mg/dL)'].append(avg)
        elif val == '_250':
            results['[Morning](CGM > 250 mg/dL)'].append(
                avg)
        elif val == '_70_180':
            results['[Morning](CGM >= 70 mg/dL and CGM <= 180 mg/dL)'].append(
                avg)
        elif val == '_70_150':
            results['[Morning](CGM >= 70 mg/dL and CGM <= 150 mg/dL)'].append(
                avg)
        elif val == '_70':
            results['[Morning](CGM < 70 mg/dL)'].append(avg)
        elif val == '_54':
            results['[Morning](CGM < 54 mg/dL)'].append(avg)

    for val, lst in a_night_p.items():
        sum = 0
        for item in lst:
            sum += item
        avg = sum / len(lst)

        if val == '_180':
            results['[Night](CGM > 180 mg/dL)'].append(avg)
        elif val == '_250':
            results['[Night](CGM > 250 mg/dL)'].append(avg)
        elif val == '_70_180':
            results['[Night](CGM >= 70 mg/dL and CGM <= 180 mg/dL)'].append(
                avg)
        elif val == '_70_150':
            results['[Night](CGM >= 70 mg/dL and CGM <= 150 mg/dL)'].append(
                avg)
        elif val == '_70':
            results['[Night](CGM < 70 mg/dL)'].append(avg)
        elif val == '_54':
            results['[Night](CGM < 54 mg/dL)'].append(avg)

    results['end'].append(1.1)
    results['end'].append(1.1)
    final = pd.DataFrame(data=results)

    final.to_csv('Results.csv', header=False, index=False)
