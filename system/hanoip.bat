@echo off
echo. 
echo.
echo     _______________________________________________
echo    #                                               #
echo    #  Hi There! Welcome To Motorola Flash Tool     #
echo    #                 By S.Sapan Gajjar             #
echo    #            Adapated from Raghu varma          #
echo    #            All rights reserved 2023           #
echo    #_______________________________________________#
echo.

echo.
fastboot getvar max-sparse-size
fastboot oem fb_mode_set
fastboot flash partition gpt.bin
fastboot flash bootloader bootloader.img
fastboot flash vbmeta vbmeta.img
fastboot flash vbmeta_system vbmeta_system.img
fastboot flash radio radio.img
fastboot flash bluetooth BTFM.bin
fastboot flash dsp dspso.bin
fastboot flash logo logo.bin
fastboot flash boot boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot flash dtbo dtbo.img
fastboot flash super super.img_sparsechunk.0
fastboot flash super super.img_sparsechunk.1
fastboot flash super super.img_sparsechunk.2
fastboot flash super super.img_sparsechunk.3
fastboot flash super super.img_sparsechunk.4
fastboot flash super super.img_sparsechunk.5
fastboot flash super super.img_sparsechunk.6
fastboot flash super super.img_sparsechunk.7
fastboot flash super super.img_sparsechunk.8
fastboot flash super super.img_sparsechunk.9
fastboot flash super super.img_sparsechunk.10
fastboot erase carrier
fastboot erase userdata
fastboot erase metadata
fastboot erase ddr
fastboot oem fb_mode_clear
echo -------------------------------------------------------------------------
echo check above for any errors
echo -------------------------------------------------------------------------
pause
fastboot reboot
exit

echo.

pause
echo.
echo.
echo     _________________________________
echo    #                                 #
echo    #  Stock Rom Successfully Flashed #
echo    #  Have a great day peace..!!     #
echo    #_________________________________#
echo.
pause
