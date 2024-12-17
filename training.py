import pymc3 as pm

if __name__ == '__main__':  # 추가된 부분
    # PyMC3 모델 생성 예제
    with pm.Model() as model:
        mu = pm.Normal('mu', mu=0, sigma=1)  # 예시 변수
        trace = pm.sample(1000)  # 샘플링 수행
    
    print("Sampling completed successfully!")

