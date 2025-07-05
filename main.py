# Diskfetch                                                          #
# Have a quick look for your disk info and ASCII Logo of disk maker. #
# LICENCE: GPL v3                                                    #
# Copyright (C) 2025 HOE Software Team.                              #


import platform
import wmi



# 制造商 ASCII Logo
MANUFACTURER_LOGOS = {
    "western digital": r"""
   .,:,,,:,:.          :::,:,::,        ,:,,::,:,  
aMMMMMMMMMMMM2      MMMMMMMMMMMMW    MMMMMMMMMMMMB
@MMMMMMMMMMMMM     .MMMMMMMMMMMMM    MMMMMMMMMMMMM
  aMMMMMMMMMMM       XMMMMMMMMMMM     i@MMMMMMMMMM
    7MMMMMMMMM         :WMMMMMMMM        ZMMMMMMMM
      :WMMMMMM            ZMMMMMM          SMMMMMM
         ZMMMM              XMMMM:           :2aX 
           SMMMr              ,MMM2               
             rMMMM@BWBBBBBBB8r  :@MMM@WBB0B8088Z2 
               :WMMMMMMMMMMMMMM    0MMMMMMMMMMMMMM
                  ZMMMMMMMMMMMM      XMMMMMMMMMMMM
                    7MMMMMMMMMM        i@MMMMMMMMM
                      :WMMMMMMM          .0MMMMMMM
                         0MMMM8             2MMMMW
                                              ..  
    """,
    "seagate": r"""
                   :                              
               SMMMM         .irXXX7;,            
           ,8MMMa.     70MMMMMMMMMMMMMMMM@2:      
         ZMMM;    .aMMMMMBS:        :XBMMMMMM0,   
      ,MMMX    XMMMMB7                   8MMMMMW  
    .MMM,   7MMMMr       70MMMMMWS.        MMMMMM 
   ZMMi   SMMM,      XMMMMMMMMMMMMMB        MMMMMM
  MMM    MMMS    i0MMMMM2.     WMMMM:       BMMMMM
 BMM     MMMMMMMMMMMZ:        rMMMMM        MMMMMM
ZMMM     ,BMMMMMZi         :0MMMMM2        SMMMMMM
MMMM                   .SMMMMMMM7         XMMMMMM 
XMMMM7             iaMMMMMMM@X           WMMMMMMX 
 rMMMMMMZS777SZWMMMMMMMM@2.            8MMMMMMM:  
  .8MMMMMMMMMMMMMMMM07.             :BMMMMMMM2    
     .ra8WWW0ZSr.                .aMMMMMMMMZ      
                              :aMMMMMMMMM7        
                          :2@MMMMMMMMMZ,          
                      XMMMMMMMMMMMMZ:             
                      ;MMMMMMMMWX                 
                       BMMMZr                     
    """,
    "samsung": r"""
 :0MMMMM@X     iWWWWW@     .@WBWW8   8WWBWM     2MMMMMM0    rMWM   @W@X   7MBWWW   WWMX    r0MMMMM8 
MMMMr 7MMMX    MMMBMMMZ    ,MMM@MM   MMBMMM.   MMMM  MMMM   aMMM.  MMMB   ZMMMMM0  MMM8   ZMMM7:8MMM
XMMM@r         MMM iMMM    ,MMM MM7 XMM MMM,   WMMMa        XMMM   MMMZ   SMM0 MM  MMM2   @MMM   , . 
  .2MMMMB;    0MMM  MMM;   :MMM 2MM MMX MMM,     ;WMMMM2    XMMM   MMMZ   2MMM ZMM WMM2   WMMM aMM@W
aXi;  ;MMMM   MMM8  MMMM   ;MMM  MMrMM  MMM;   Zri   WMMM   SMMM   MMM8   SMMM  MMX0MM2   @MMM   MMM
MMMMB.iMMMW  0MMM:  aMMM;  XMMM  MMMMM  MMMX   MMMMi.WMMM   iMMMBr8MMMX   8MMM  :MMMMM8   2MMMZX@MMM
 .ZMMMMM8r   8008    B8BX  ;000  i000:  B00;    XBMMMMBX     ,a@MMMMZi    ;ZaZ   Xaa2Z;    ,SWMMM07 
    """,
    "kingston": r"""
               ,;7SaZ80BWB@@@@MMMMMWBZ27:         
          ,;r7r;i:..                 .,iirS       
        ,M.             .rSXi...,:i:      M;      
         MiirXSZX    :20Zr   i72ar.i.   BM0a      
        MX7i:   X,  iZ7  ;WMMMMMMM      MMM,      
       XM MMMMM:                        7MM       
        M  WMMMM                  :      MM       
        M8  7MMM2                0ar,    MM       
        .MX   MMM                  SMMMMMMM       
          BWr  ZMZ             ;28Z2Z@MMMMa       
            MM27MM   .:ir72Z@MBSXrr7XXXWMM.       
            M  .7MMMMMMMMMMMMMMMMMW8Sr,XMM        
           ZM    WMMMMMMMMMMMMMWX.     0M:        
           Mr     MMMMMMMMMMMM     .XMMMW         
          rM      WMMMMMMMMMMMBMMMMMMMMW          
          MZ       MMWMMMMMMMMMMMMW2ZS.           
          M        WMZ  ZMMMMMMMMMM               
         @@        .MM     2MMMMMMMM.             
         M,         MMM      MMMMMMMMi            
        2M           MMr     MMMrWMMMM;           
        M;           WMM     WMB  ,WMMMr          
       iM  ........  .MMa    ZM     ;MMMS         
    """,
    "hitachi": r"""
MMMMS       :MMMM   MMMM XMMMMMMMMMMMMMMMM   BMMMMM:        7WMMMMMMMMM0r   iMMMM        MMMM   0MMM
MMMMX       .MMMM   MMMM  riii:;MMMM,:ii;;  WMMMaMMMi     aMMMMr.   .ZMMMM, iMMMM        MMMM   WMMM
MMMMa.:iii:,rMMMM   MMMM        MMMM       WMMM  SMMM;   SMMMM        irrS: ,MMMM ,iiii:.MMMM   8MMM
MMMMMMMMMMMMMMMMM   MMMM        MMMM      MMMM    XMMM7  MMMMX              ,MMMMMMMMMMMMMMMM   8MMM
MMMMr        MMMM   MMMM        MMMM     MMMMMWMMM@MMMMX 7MMMM        X88@X ,MMM@        MMMM   8MMM
MMMM2       ,MMMM   MMMM        MMMM   .MMMMXr22a2Xi@MMMZ 2MMMMX:   :0MMMM: iMMMM        MMMM   WMMM
MMMMS       :MMMM   MMMM       .MMMM   MMMMX         MMMMS  r0MMMMMMMMM8i   iMMM@        MMMM   8MMM
    """,
    "toshiba": r"""
MMMMMM@MMMMMM8  i8@MMMMMMMZi    i0MMMMMMMMZ    MMMM     MMMM   :MMMM   rMM@MMMMM@BS      ;MMMMMM    
MMMMMMMMMMMMM0 ZMMMMMWWMMMMMZ  SMMMMX7XWMMMM   MMMM     MMMM   iMMMM   XMMMM00BMMMMM     MMMMMMMM   
     MMMM      MMMM.    ,MMMM  BMMM0    i,     MMMMXrX77MMMM   :MMMM   rMMMB   iMMMB    WMMM 7MMM2  
     MMMM      MMMM      MMMM   SBMMMMMMMMM7   MMMMMMMMMMMMM   ,MMMM   ;MMMMMMMMMM8    rMMM0  MMMM. 
     MMMM.     MMMM:    iMMMM  i:i;     MMMM.  MMMM, . .MMMM   :MMMM   rMMM8    MMMM,  MMMMMMMMMMMM 
    .MMMM:     aMMMMMMMMMMMMa  0MMMM0ZZBMMMM   MMMM     MMMM   iMMMM   XMMMMMMMMMMMM. MMMM8SZaSWMMMZ
     MWWM.      :ZWMMMMMMWa:    r8WMMMMM@0X    @WWM     @WWM   :MWWW   ;MWB@MMMMW8X  ;M@WB      WWW@

""",
    "hp": r"""
                  .     MMMW8Xi                   
               ,SM;     MMMMMMMM@07               
            7@MMMM     MMMMMMMMMMMMMMWr           
          8MMMMMM     aMMMMMMMMMMMMMMMMMZ         
        BMMMMMMM2     MMMMMMMMMMMMMMMMMMMM8       
      XMMMMMMMMM     MMMMMMMMMMMMMMMMMMMMMMMr     
     WMMMMMMMMM,    XMMMMMMMMMMMMMMMMMMMMMMMM0    
    MMMMMMMMMM0    ,MMMMMMMMMMMMMMMMMMMMMMMMMMM   
   MMMMMMMMMMM     S@008BMMMMMMMWZ888Z8Z880WMMMM  
  BMMMMMMMMMMr            :MMMMM             0MMZ 
  MMMMMMMMMMM     SXSS     MMMM:    .XX2:     MMM 
 WMMMMMMMMMM     ZMMM8    .MMMB     MMMM     0MMM2
.MMMMMMMMMMS     MMMM     MMMM     ZMMM;    :MMMM@
8MMMMMMMMMM     MMMM     aMMMX    .MMM@     MMMMMM
MMMMMMMMMM,    rMMMa     MMMM     MMMM     aMMMMMM
MMMMMMMMM0     MMMM     MMMM     SMMMS     MMMMMMM
8MMMMMMMM     BMMM:    rMMMa     MMMM     MMMMMMMM
 MMMMMMM;    :MMMB     MMMM     MMMM     XMMMMMMM@
 BMMMMM@     MMMM     BMMM:    aMMM8     MMMMMMMMS
  MMMMM     aMMMi    ,MMMB     X7rr     WMMMMMMMM 
  BMMM:     MMMZ     MMMM              XMMMMMMMMZ 
   MMMaZ80ZMMMM8a888WMMMr    ,B080808WMMMMMMMMMM  
    MMMMMMMMMMMMMMMMMMMM     MMMMMMMMMMMMMMMMMM   
     WMMMMMMMMMMMMMMMMM     SMMMMMMMMMMMMMMMM0    
      XMMMMMMMMMMMMMMMa     MMMMMMMMMMMMMMMMr     
        8MMMMMMMMMMMMM     MMMMMMMMMMMMMMMZ       
          ZMMMMMMMMMM,    rMMMMMMMMMMMMMZ         
            ;WMMMMMM0     MMMMMMMMMMMBi           
                iSB@     WMMM@@B8X:               
    """,
    "default": r"""
                                    .i;r;i.       
                                 .irSa8ZZ2S7i     
                                .;XSX7;;;7XaXi.   
                                :XZ27.   .7ZZ7:   
                                :SZZr.   .7ZZX,   
                                ,;7r:   :rSSX:.   
                                      ,7SaSr.     
            . . . . . . . . . .      :72ZaX:       
         ..:,:,:,,,,,,,,,,,,,:,,...,:r7SX7i.       
        ,,:,:,:,:::,:,:,:,:::::,:,,,::i::..        
       ........................... ..:::,,         
                                    i72227i       
   .:iii:i:iiiii:i:::i:i:::i:i:i,,.ir2Z0Za7i      
  iX80BBWBBBWBWBB0B0B0B0B0B0BBW00Z2XX7X7XXXri.    
 .;8@MMMMMMM@MMMMMMMMMMMMMMMMMMMMMW027;;;XSaXi    
  ;aW@MMM@BaXXa0MMMMMMM@MMMMMMMMMMMB8a2X22ZZ2i.   
  :S8BW@@W82XX20B@WWBWBWBWBWBWBWW@WWBB0B0B00Si    
  :X80BBWBB00800BBB0B0B0B0B0B0B0BBBBWBWWWBBZX:    
  :XaZZZZZZ88088ZZaZaZZZaZZZZZaZaZaZZ8Z088ZZ7,    
  ,rXX7r7r77777r7r7r7r7r7r7r7r7r7r7r7r7777XXr.    
   ,,,.....................................,.     
    """
}



def get_disk_info():
    """获取物理磁盘信息"""
    disks = []

    if platform.system() == "Windows":
        try:
            c = wmi.WMI()
            for physical_disk in c.Win32_DiskDrive():
                model = physical_disk.Model.strip()
                serial = physical_disk.SerialNumber.strip()
                size = int(physical_disk.Size) // (1024 ** 3) if physical_disk.Size else 0

                # 磁盘类型识别
                model_upper = model.upper()
                if "SSD" in model_upper or "SOLID" in model_upper:
                    disk_type = "SSD"
                elif "NVMe" in model_upper or "M.2" in model_upper:
                    disk_type = "NVMe SSD"
                elif "HDD" in model_upper or "HARD" in model_upper:
                    disk_type = "HDD"
                else:
                    if any(x in model_upper for x in ("SSD", "FLASH", "SATA")):
                        disk_type = "SSD"
                    elif any(x in model_upper for x in ("HDD", "HARD", "DISK")):
                        disk_type = "HDD"
                    elif "USB" in model_upper or "EXTERNAL" in model_upper:
                        disk_type = "External/USB"
                    else:
                        disk_type = "Unknown"

                disks.append({
                    "model": model,
                    "serial": serial,
                    "size": size,
                    "type": disk_type,
                    "device_id": physical_disk.DeviceID
                })
        except Exception as e:
            print(f"获取磁盘信息时出错: {str(e)}")
            return []

    return disks


def get_manufacturer_logo(model):
    """根据型号匹配制造商 Logo"""
    if not model:
        return MANUFACTURER_LOGOS["default"]

    model_lower = model.lower()

    # 改进制造商识别
    if "western" in model_lower or "wd" in model_lower:
        return MANUFACTURER_LOGOS["western digital"]
    elif "seagate" in model_lower:
        return MANUFACTURER_LOGOS["seagate"]
    elif "samsung" in model_lower:
        return MANUFACTURER_LOGOS["samsung"]
    elif "kingston" in model_lower:
        return MANUFACTURER_LOGOS["kingston"]
    elif "hitachi" in model_lower or "hgst" in model_lower:
        return MANUFACTURER_LOGOS["hitachi"]
    elif "toshiba" in model_lower:
        return MANUFACTURER_LOGOS["toshiba"]
    elif "hp" in model_lower:
        return MANUFACTURER_LOGOS["hp"]
    elif "pioneer" in model_lower:
        return MANUFACTURER_LOGOS["default"]
    elif "external" in model_lower or "usb" in model_lower:
        return MANUFACTURER_LOGOS["default"]
    else:
        return MANUFACTURER_LOGOS["default"]


def display_disk_info(disk, index, total):
    """显示单个磁盘的详细信息"""
    # 获取制造商Logo
    logo = get_manufacturer_logo(disk["model"])

    # 提取实际制造商名称
    model_parts = disk["model"].split()
    manufacturer = model_parts[0] if model_parts else "Unknown"

    # 格式化输出
    print(f"\n{logo}")
    print(f" 磁盘 {index + 1}/{total} ".center(60, "="))
    print(f" 制造商: {manufacturer}")
    print(f" 型号: {disk['model']}")
    print(f" 序列号: {disk['serial']}")
    print(f" 类型: {disk['type']}")
    print(f" 容量: {disk['size']} GB")


def display_diskfetch():
    """信息面板"""
    disks = get_disk_info()

    if not disks:
        print("未检测到磁盘设备")
        return

    total_disks = len(disks)

    # 显示所有磁盘信息
    for i, disk in enumerate(disks):
        display_disk_info(disk, i, total_disks)

        # 分隔线
        if i < total_disks - 1:
            print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    display_diskfetch()
    input('\n\n\n---------- 按下 "ENTER" 退出 ----------')