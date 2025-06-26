#  Web Crawler Monitor

Plataforma simples para monitorar concorrentes automaticamente por meio de rastreadores web, com agendamento personalizável e geração de insights simulados.

##  Funcionalidades
- Rastreamento de URLs com frequência configurável
- Agendamento automático com APScheduler
- Pausar, retomar, editar ou remover tarefas
- Simulação de geração de insights

##  Como rodar

```bash
git clone https://github.com/SEU_USUARIO/web-crawler-monitor.git
cd web-crawler-monitor
pip install -r requirements.txt
python crawler/web_crawler.py
```

## Requisitos

- Python 3.8+
- requests
- beautifulsoup4
- apscheduler
