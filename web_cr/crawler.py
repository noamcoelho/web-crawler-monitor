import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
import time
import uuid

# Dicionário que manterá os jobs de rastreamento
tracking_jobs = {}

# Inicializa o scheduler
scheduler = BackgroundScheduler()
scheduler.start()

def crawler(url):
    try:
        print(f"Rastreamento iniciado para: {url}")
        print("------------------------------")
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Exemplo simples de "insight"
        title = soup.title.string if soup.title else "Sem título"
        word_count = len(soup.get_text().split())

        print(f"Insight gerado: Título = {title}, Palavras = {word_count}")
        print("------------------------------")
    except Exception as e:
        print(f"Erro ao rastrear {url}: {e}")
        print("------------------------------")

def schedule_tracking(url, interval_seconds):
    job_id = str(uuid.uuid4())
    job = scheduler.add_job(crawler, 'interval', [url], seconds=interval_seconds, id=job_id)
    tracking_jobs[job_id] = {"url": url, "interval": interval_seconds}
    print(f"Rastreio agendado: {url} a cada {interval_seconds} segundos [ID: {job_id}]")
    print("------------------------------")
    return job_id

def pause_tracking(job_id):
    job = scheduler.get_job(job_id)
    if job:
        job.pause()
        print(f"Rastreio pausado [ID: {job_id}]")
        print("------------------------------")

def resume_tracking(job_id):
    job = scheduler.get_job(job_id)
    if job:
        job.resume()
        print(f"Rastreio retomado [ID: {job_id}]")
        print("------------------------------")

def edit_tracking(job_id, new_interval):
    job = scheduler.get_job(job_id)
    if job:
        job.reschedule(trigger='interval', seconds=new_interval)
        tracking_jobs[job_id]['interval'] = new_interval
        print(f"Rastreio editado [ID: {job_id}] Novo intervalo: {new_interval}s")
        print("------------------------------")

def remove_tracking(job_id):
    job = scheduler.get_job(job_id)
    if job:
        job.remove()
        tracking_jobs.pop(job_id, None)
        print(f"Rastreio removido [ID: {job_id}]")
        print("------------------------------")

# Demonstração
if __name__ == "__main__":
    url = "https://example.com"
    job_id = schedule_tracking(url, 30)  # 30 segundos de intervalo

    # Demonstra controle via código (simulação)
    time.sleep(90)
    pause_tracking(job_id)
    time.sleep(10)
    resume_tracking(job_id)
    time.sleep(10)
    edit_tracking(job_id, 60)
    time.sleep(70)
    remove_tracking(job_id)
    scheduler.shutdown()
