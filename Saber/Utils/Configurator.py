import yaml
import discord

# Попытка получения конфигурации
try:
    # Подключение файла конфигурации
    __temp__ = open('./Config/master.yml', 'r', encoding='utf-8')
    # Загрузка данных из файла конфигурации
    master = yaml.safe_load(__temp__)
    cfg = master['CONFIG'.upper()]
    # Получаем список серверов из белого списка и превращаем в кортеж
    whitelist = tuple(master['WHITELIST'.upper()])
    # Получаем список игнорируемых каналов (не будет считаться уровень) и превращаем в кортеж
    IGNORED_CHANNELS = tuple(master['IGNORED_CHANNELS'])
    # Получаем список модулей, включаемых при загрузке и превращаем в кортеж
    INITIAL_COGS = tuple(master['INITIAL_COGS'])
    # Удаление временных данных
    __temp__.close()
    del __temp__
    # Переменные данных конфигурации
    BOT_PREFIX = cfg['PREFIX']
    BOT_STATUS = cfg['STATUS']
    BOT_MAINTAINERS = tuple(cfg['MAINTAINERS'])
    BOT_IS_NO_PERMS_MSG_ENABLED = cfg['SHOW_NO_PERMS_MESSAGES']
    MAIN_LOGS_CHANNEL = cfg['LOG_CHANNEL_ID']
    XP_LOGS_CHANNEL = cfg['XP_LOG_CHANNEL_ID']
    GIPHY_API = cfg['GIPHY_API_KEY']
    GENIUS_API_KEY = cfg['GENIUS_API_KEY']
    DEFAULT_STATUS = discord.Activity(
        name=BOT_STATUS + f' | {BOT_PREFIX}help', url="https://twitch.tv/defracted",
        type=discord.ActivityType.streaming)
except Exception as err:
    print(err)

# Загрузка описаний команд
try:
    # Подключение файла конфигурации
    __temp__ = open('./Config/commands-information.yml', 'r', encoding='utf-8')
    # Загрузка данных из файла конфигурации
    CMD_INFO = yaml.safe_load(__temp__)
    CMD_INFO = CMD_INFO['COMMANDS']
    # Удаление временных данных
    __temp__.close()
    del __temp__
except Exception as err:
    print(err)


def find_prefixes(message):
    try:
        # Подключение файла конфигурации префиксов
        with open(f'./Config/{message}/guildSettings.yml', 'r', encoding='utf-8') as prefixes_cfg:
            prefixes = yaml.safe_load(prefixes_cfg)
            return prefixes['PREFIX']
    except Exception as err:
        raise err