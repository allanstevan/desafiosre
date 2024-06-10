### Desafio SRE - Serviços de Mensageria

#### Cenário

Você foi contratado como SRE em uma empresa que usa serviços de mensageria para gerenciar a comunicação assíncrona entre microserviços. O sistema precisa ser altamente disponível e resiliente, pois suporta aplicações críticas de negócios.

#### Escolha de Tecnologia

Você pode escolher uma das seguintes tecnologias para realizar o desafio:

-   RabbitMQ

-   Kafka

-   Amazon SQS

-   Amazon SNS

-   Azure Event Hub

-   Qualquer outra tecnologia equivalente

Refira-se à seção **Recursos** abaixo para sugestões de scripts produtores e consumidores.

#### Tarefas

1.  Instalação e Configuração Básica

-   Instalação e Configuração: Instale e configure o serviço de mensageria escolhido. Se estiver usando um serviço gerenciado na nuvem (como SQS, SNS ou Event Hub), configure o serviço para alta disponibilidade e durabilidade das mensagens.

-   Documentação: Documente o processo de instalação e configuração, incluindo as opções escolhidas para garantir a alta disponibilidade e resiliência.

2.  Monitoramento e Alerta

-   Configure ferramentas de monitoramento (por exemplo, Prometheus e Grafana para serviços locais, ou CloudWatch para serviços AWS) para coletar métricas de desempenho e disponibilidade do serviço de mensageria escolhido.

-   Crie dashboards para visualizar as métricas mais importantes, como latência, throughput, uso de CPU/memória, etc. (opcional)

-   Configure alertas para situações críticas, como falha de componentes, aumento de latência, filas crescendo indefinidamente, etc. (opcional)

3.  Teste de Resiliência

-   Simule falhas no serviço de mensageria e observe o comportamento do sistema. Documente suas observações e explique como o sistema se recupera das falhas.

-   Realize testes de carga para avaliar o desempenho do serviço sob alta carga. Use ferramentas como Apache JMeter ou locust.io para gerar a carga (ou scripts personalizados se estiver usando serviços na nuvem). Documente os resultados e qualquer problema de desempenho identificado. (opcional)

4.  Otimização e Melhores Práticas

-   Identifique possíveis pontos de falha e gargalos no serviço de mensageria escolhido e proponha melhorias.

-   Documente as melhores práticas para configuração, operação e manutenção do serviço de mensageria escolhido.

5.  Backup e Recuperação

-   Configure um processo de backup regular para os dados, se aplicável (opcional).

-   Descreva um plano de recuperação de desastres que inclua procedimentos para restaurar os dados a partir dos backups em caso de perda total de dados (opcional).

#### Entregáveis

1.  Documentação detalhada da instalação e configuração do serviço de mensageria escolhido.

2.  Dashboards de monitoramento e configurações de alertas. (opcional)

3.  Relatórios de testes de resiliência e carga, incluindo observações e recomendações. (opcional)

4.  Documentação das melhores práticas e propostas de melhorias.

5.  Procedimentos de backup (se aplicável) e plano de recuperação de desastres. (opcional)

#### Critérios de Avaliação

-   Precisão Técnica: Correção e eficácia das configurações e scripts fornecidos.

-   Documentação: Clareza, detalhamento e organização da documentação entregue.

-   Monitoramento e Alerta: Adequação das métricas monitoradas e eficácia dos alertas configurados.

-   Resiliência e Desempenho: Capacidade de identificar e resolver problemas durante os testes de falha e carga.

-   Melhores Práticas: Qualidade das sugestões de melhorias e adoção de práticas recomendadas.

#### Recursos

V. encontrará exemplos de script para produzir e consumir filas neste diretório. É franqueado ao candidato a customização dos mesmos de acordo com suas preferências.

consumer_rabbitmq.py
consumer_sqs.py
kafka_consumer.py
kafka_producer.py
producer_rabbitmq.py
producer_sqs.py
