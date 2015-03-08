# -*- coding: utf-8 -*-
import os
# MODE 列表
MODE_DEV = 'DEV'    # 开发环境
MODE_PRO = 'PRO'

MODE = os.environ.get('MODE') or MODE_DEV

