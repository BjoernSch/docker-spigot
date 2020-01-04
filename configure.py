#! /usr/bin/env python3

import os
import datetime
class Config:
    def __init__(self):
        self.properties = self._set_props()
        return

    @staticmethod
    def _set_props():
        props = {
            "generator-settings": os.getenv("GENERATOR_SETTINGS"),
            "os-permission-level": os.getenv("OP_PERMISSION_LEVEL", 4),
            "allow-nether": os.getenv("ALLOW_NETHER", "true"),
            "level-name": os.getenv("LEVEL_NAME", "world"),
            "enable-query": os.getenv("ENABLE_QUERY", "false"),
            "allow-flight": os.getenv("ALLOW_FLIGHT", "false"),
            "prevent-proxy-connections": os.getenv("PREVENT_PROXY_CONNECTIONS", "false"),
            "server-port": os.getenv("SERVER_PORT", 25565),
            "max-world-size": os.getenv("MAX_WORLD_SIZE", 29999984),
            "level-type": os.getenv("LEVEL_TYPE", "DEFAULT"),
            "enable-rcon": os.getenv("ENABLE_RCON", "false"),
            "level-seed": os.getenv("LEVEL_SEED"),
            "force-gamemode": os.getenv("FORCE_GAMEMODE", "false"),
            "server-ip": os.getenv("SERVER_IP"),
            "network-compression-threshold": os.getenv("NETWORK_COMPRESSION_THRESHOLD", 256),
            "spawn-npcs": os.getenv("SPAWN_NPCS", "true"),
            "max-build-height": os.getenv("MAX_BUILD_HEIGHT", 256),
            "white-list": os.getenv("WHITE_LIST", "false"),
            "spawn-animals": os.getenv("SPAWN_ANIMALS", "true"),
            "hardcore": os.getenv("HARDCORE", "false"),
            "snooper-enabled": os.getenv("SNOOPER_ENABLED", "true"),
            "resource-pack-sha1": os.getenv("RESOURCE_PACK_SHA1"),
            "online-mode": os.getenv("ONLINE_MODE", "true"),
            "resource-pack": os.getenv("RESOURCE_PACK"),
            "pvp": os.getenv("PVP", "true"),
            "difficulty": os.getenv("DIFFICULTY", 1),
            "enable-command-block": os.getenv("ENABLE_COMMAND_BLOCK", "false"),
            "gamemode": os.getenv("GAMEMODE", 0),
            "player-idle-timeout": os.getenv("PLAYER_IDLE_TIMEOUT", 0),
            "max-players": os.getenv("MAX_PLAYERS", 20),
            "max-tick-time": os.getenv("MAX_TICK_TIME", 60000),
            "spawn-monsters": os.getenv("SPAWN_MONSTERS", "true"),
            "view-distance": os.getenv("VIEW_DISTANCE", 10),
            "generate-structures": os.getenv("GENERATE_STRUCTURES", "true"),
            "motd": os.getenv("MOTD", "A Minecraft server (SpigotMc) powered by Docker (image: bjoernsch/spigot)")
        }
        return props

    def write(self, file="server.properties"):
        with open(file, 'w') as f:
            now = datetime.datetime.now().isoformat()
            f.write("# Minecraft server properties\n")
            f.write("# Automatically generated at {}\n\n".format(now))
            for k,v in self.properties.items():
                if not v:
                    f.write('{}:\n'.format(k))
                elif isinstance(v, (int)):
                    f.write('{}: {}\n'.format(k, v))
                else:
                    f.write('{}: {}\n'.format(k, v))
        return

if __name__ == "__main__":
    c = Config()
    c.write("/data/server.properties")
