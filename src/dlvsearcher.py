import pyperclip, webbrowser

webbrowser.open("https://tmstracking.dhl.com/tracking/web/seguimiento/resultados.asp?param_cod_plantilla=&pruebas=&asp_origen=busqueda.asp&cod_cliente=&cod_cia=&num_de_remito=&num_de_pedido={}".format(pyperclip.paste()))