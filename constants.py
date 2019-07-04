CSV_SEP = ','


kpi_rate = [1, 0.5, 0.6, 0.5, 0.6, 0.6, 0.6]

col_total = 'KPI'

csv_encoding = 'Shift_JISx0213'
csv_path = '..\\data\\**\\E_Detail*.csv'
necessary_columns = ['集計日', '教科', '設問番号', '設問種別', '採点完了件数', '2回目採点待ち残数', '否認採点待ち残数', '検知採点待ち残数', '類型不一致採点待ち残数', '正誤不一致採点待ち残数', 'リーダー待ち残数']
kpi_columns = ['採点完了件数', '2回目採点待ち残数', '否認採点待ち残数', '検知採点待ち残数', '類型不一致採点待ち残数', '正誤不一致採点待ち残数', 'リーダー待ち残数']

classify = ['集計日', '教科', '設問番号', '設問種別']


shown_columns = {'集計日' : 'Date',
				 '教科' : 'Class-1',
				 '設問番号' : 'Class-2',
				 '設問種別' : 'Class-3',
				 '採点完了件数' : 'Col-1',
				 '2回目採点待ち残数' : 'Col-2',
				 '否認採点待ち残数' : 'Col-3',
				 '検知採点待ち残数' : 'Col-4',
				 '類型不一致採点待ち残数' : 'Col-5',
				 '正誤不一致採点待ち残数' : 'Col-6',
				 'リーダー待ち残数' : 'Col-7'}

shown_value_Class1 = {'国' : 'JA',
					  '社' : 'SS',
					  '数' : 'MA',
					  '理' : 'SC',
					  '英' : 'EN'}

shown_value_Class3 = {'M' : 'MA',
					  '短' : 'SD',
					  '記' : 'DE'}